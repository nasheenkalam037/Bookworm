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
from save_book import save_book

# Mutex for printing to the console
print_lock = threading.Lock()
# Mutex for updating the count variable
shared_mutex = threading.Lock()
count = 0

IMAGE_FOLDER = '../web/public/images/book_covers'

book_queue = Queue()
tcp = None
SLEEP_TIME = 5
NUM_THREADS = 2

DEBUG = 0

def worker_thread(thread_id):
    global count

    with print_lock:
        print(f'[Thread {thread_id}] Starting Thread')
    while True:
        book = book_queue.get()
        if book is None:
            break
        with print_lock:
            print(f'[Thread {thread_id}] Working on task {book["book_id"]} by {book["amazon_link"]}')

        error = getInfo.get_amazon_book_cover(thread_id, book["amazon_link"], book["book_id"], IMAGE_FOLDER)

        book_queue.task_done()
        if error == '':
            with print_lock:
                print(f'[Thread {thread_id}] Task Completed: {book["book_id"]} (Queue size { book_queue.qsize()})')
        else:
            with print_lock:
                print(f'[Thread {thread_id}] Task Failed: {book["book_id"]} with error: {error} (Queue size { book_queue.qsize()})')
        
        time.sleep(SLEEP_TIME)

    with print_lock:
        print(f'[Thread {thread_id}] Thread Ended')


def setup_db():
    global tcp
    params = config()
    tcp = ThreadedConnectionPool(1, 10, **params)
    print('[SETUP] TCP returned:', tcp)

def grab_book_covers():
    global tcp, count
    start = time.time()
    try:
        setup_db()

        # Grab all book ids and amazon links
        conn = tcp.getconn()
        cur = conn.cursor()
        cur.execute('SELECT book_id, amazon_link FROM "public"."BookDetails"')
        data = cur.fetchall()
        tcp.putconn(conn)

        if data == None:
            raise Exception('Unable to grab books from database!')
        
        task_num = 1
        for d in data:
            if DEBUG > 1:
                with print_lock:
                    print(f'[Main Thread] Adding Book {task_num}/{len(books_to_search)} to queue:', d[0], d[1])
            task_num += 1
            book_queue.put({'book_id':d[0], 'amazon_link':d[1]})
        for i in range(NUM_THREADS):
            book_queue.put(None)

        # print(books_to_search)

        for i in range(NUM_THREADS):
            t = threading.Thread(target=worker_thread, args=(i, ))
            # t.daemon = True
            t.start()


        with print_lock:
            print(f'[Main Thread] Waiting for all {task_num-1} tasks to be marked complete')
        book_queue.join()
        print(threading.enumerate())

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
    grab_book_covers()
