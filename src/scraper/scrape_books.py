#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psycopg2
import requests
import xmltodict
import unidecode
import threading
import csv
import time
from datetime import datetime
import sys
from queue import Queue
from psycopg2.pool import ThreadedConnectionPool
# Local Files
from config import config
import get_book_information as getInfo

# Mutex for printing to the console
print_lock = threading.Lock()
# Mutex for updating the count variable
shared_mutex = threading.Lock()
count = 0

book_queue = Queue()
tcp = None
SLEEP_TIME = 2
NUM_THREADS = 10

DEBUG = 0


def worker_thread(thread_id):
    global count

    with print_lock:
        print(f'[Thread {thread_id}] Starting Thread')
    while True:
        with print_lock:
            print(f'[Thread {thread_id}] Waiting for next Task (Queue size { book_queue.qsize()})')

        book = book_queue.get()
        # print(book)
        if book is None:
            break

        with print_lock:
            print(f'[Thread {thread_id}] Working on task {book["title"]} by {book["author"]}')

        search_result = getInfo.search_amazon_for_book(thread_id, book['title'], book['author'])

        status = False
        if search_result:
            status = getInfo.fetch_new_book_info(thread_id, search_result)

            # If the status is good, increase the number of books added
            if status:
                with shared_mutex:
                    count += 1

        book_queue.task_done()
        with print_lock:
            print(f'[Thread {thread_id}] Task Completed: {book["title"]}; Status: {status}')
        time.sleep(SLEEP_TIME)

    with print_lock:
        print(f'[Thread {thread_id}] Thread Ended')


def setup_db():
    global tcp
    params = config()
    tcp = ThreadedConnectionPool(1, 10, **params)

    print('[SETUP] TCP returned:', tcp)

def remove_already_found_books(books_to_search):
    '''
    Given a list of books, this function will get all books from the database and 
    remove the books that match based on title.
    '''
    conn = tcp.getconn()
    cur = conn.cursor()
    
    cur.execute('SELECT title FROM "public"."Books"')
    
    data = cur.fetchall()
    tcp.putconn(conn)

    if data != None:
        for title in data:
            books_to_remove=[]
            for book in books_to_search:
                if book['title'] == 'title':
                    books_to_remove.append(book)
            for b in books_to_remove:
                books_to_search.remove(b)

    return books_to_search


def scrap_books():
    global tcp, count
    start = time.time()
    try:
        setup_db()

        # read books from CSV file
        books_to_search = []
        with open('books.csv', newline='') as f:
            reader = csv.reader(f)
            skip_first_row = True
            for row in reader:
                # Skip heading
                if skip_first_row:
                    skip_first_row = False
                    continue
                
                # Add new book
                books_to_search.append({'title':row[1], 'author':row[0]})

        # print(books_to_search)
        # grab all books from the database
        # remove any books that have been already added OR mark them as to be updated
        books_to_search = remove_already_found_books(books_to_search)

        # print(books_to_search)

        for i in range(NUM_THREADS):
            t = threading.Thread(target=worker_thread, args=(i, ))
            # t.daemon = True
            t.start()

        task_num = 1
        for d in books_to_search:
            if DEBUG > 1:
                with print_lock:
                    print(f'[Main Thread] Adding Book {task_num}/{len(books_to_search)} to queue:', d[0], d[1])
            task_num += 1
            book_queue.put(d)

        with print_lock:
            print(f'[Main Thread] Waiting for all {task_num-1} tasks to be marked complete')
        book_queue.join()
        print(threading.enumerate())

        # Kill all of the threads
        for i in range(NUM_THREADS):
            book_queue.put(None)
        book_queue.join()

    except (Exception, psycopg2.DatabaseError) as error:
        with print_lock:
            print('[scrap_books] ERROR:', error)
    finally:
        with print_lock:
            print('')
        if tcp is not None:
            tcp.closeall()
            with print_lock:
                print('Database connection closed.')
        with print_lock:
            print("Added {} books".format(count))
            print("Execution time = {0:.5f}s".format(time.time() - start))
            print("Execution date = {}".format(datetime.now()))


if __name__ == '__main__':
    scrap_books()
