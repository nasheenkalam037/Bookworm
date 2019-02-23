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
import get_amazon_review_info as getInfo
from save_review import save_review

# Mutex for printing to the console
print_lock = threading.Lock()
# Mutex for updating the count variable
shared_mutex = threading.Lock()
count = 0

review_queue = Queue()
tcp = None
SLEEP_TIME = 5
NUM_THREADS = 1

DEBUG = 0

def worker_thread(thread_id):
    global count

    with print_lock:
        print(f'[Thread {thread_id}] Starting Thread')
    while True:
        with print_lock:
            print(f'[Thread {thread_id}] Waiting for next Task (Queue size { review_queue.qsize()})')

        review = review_queue.get()
        # print(review)
        if review is None:
            break

        # with print_lock:
        #     print(f'[Thread {thread_id}] Working on task {book["title"]} by {book["author"]}')
        # search_result = getInfo.search_amazon_for_review(thread_id, book['title'], book['author'])
        # read books url from CSV file
        books_to_search = []
        with open('book_link.csv', newline='') as f:
            reader = csv.reader(f)
            skip_first_row = True
            for row in reader:
                # Skip heading
                if skip_first_row:
                    skip_first_row = False
                    continue
                
                # Add new book review
                books_to_search.append({'book_id':row[0], 'book_link':row[1]})

        status = False
        if books_to_search:
            review_info = getInfo.fetch_new_review_info(thread_id, books_to_search)

            # If the review_info is good, increase the number of reviews added
            if review_info:
                conn = tcp.getconn()
                csv.writer('review_output.csv', review_info)
                tcp.putconn(conn)

                with shared_mutex:
                    count += 1

        review_queue.task_done()
        with print_lock:
            print(f'[Thread {thread_id}] Task Completed: {books_to_search["book_id"]}')
        time.sleep(SLEEP_TIME)

    with print_lock:
        print(f'[Thread {thread_id}] Thread Ended')


def setup_db():
    global tcp
    params = config()
    tcp = ThreadedConnectionPool(1, 10, **params)

    print('[SETUP] TCP returned:', tcp)

def scrap_review():
    global tcp, count
    start = time.time()
    try:
        setup_db()

        # read books url from CSV file
        books_to_search = []
        with open('book_link.csv', newline='') as f:
            reader = csv.reader(f)
            skip_first_row = True
            for row in reader:
                # Skip heading
                if skip_first_row:
                    skip_first_row = False
                    continue
                
                # Add new book review
                books_to_search.append({'book_id':row[0], 'book_link':row[1]})

        # print(books_to_search)
        # grab all books from the database
        # remove any books that have been already added OR mark them as to be updated
        # books_to_search = remove_already_found_books(books_to_search)

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
            review_queue.put(d)

        with print_lock:
            print(f'[Main Thread] Waiting for all {task_num-1} tasks to be marked complete')
        review_queue.join()
        print(threading.enumerate())

        # Kill all of the threads
        for i in range(NUM_THREADS):
            review_queue.put(None)
        review_queue.join()

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
    scrap_review()
