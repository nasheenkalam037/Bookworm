#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psycopg2
import re
import time
from datetime import datetime
import threading
from queue import Queue
from psycopg2.pool import ThreadedConnectionPool
# Local Files
from config import config
import get_amazon_review_info as getInfo
import save_review as setInfo

# Mutex for printing to the console
print_lock = threading.Lock()
# Mutex for updating the count variable
shared_mutex = threading.Lock()
count = 0

book_queue = Queue()
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
            print(f'[Thread {thread_id}] Waiting for next Task (Queue size { book_queue.qsize()})')

        book = book_queue.get()

        if book is None:
            break

        with print_lock:
            print(f'[Thread {thread_id}] Working on task')

        review_info = getInfo.fetch_review_data(thread_id, book)
        if review_info:
            conn = tcp.getconn()
            setInfo.save_user(conn, review_info)
            tcp.putconn(conn)

            with shared_mutex:
                count += 1

        book_queue.task_done()
        with print_lock:
            print(f'[Thread {thread_id}] Task Completed')
        time.sleep(SLEEP_TIME)

    with print_lock:
        print(f'[Thread {thread_id}] Thread Ended')

def setup_db():
    global tcp
    params = config()
    tcp = ThreadedConnectionPool(1, 10, **params)

    print('[SETUP] TCP returned:', tcp)

def scrap_amazon_reviews():
    global tcp, count
    start = time.time()
    try:  
        setup_db()

        # Fetch book_id and book_url from AmazonDetails tabel
        conn = tcp.getconn()
        cur = conn.cursor()
        cur.execute('SELECT book_id, book_link FROM "public"."AmazonDetails"')
        data = cur.fetchall()

        for i in range(NUM_THREADS):
            t = threading.Thread(target=worker_thread, args=(i, ))
            t.start()

        task_num = 1
        for d in data:
            if DEBUG > 1:
                with print_lock:
                    print(f'[Main Thread] Adding Reviews {task_num}/{len(data)} to queue:', d[0], d[1])
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

        conn.commit()
        tcp.putconn(conn)
    
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


if __name__ == "__main__":
    scrap_amazon_reviews()