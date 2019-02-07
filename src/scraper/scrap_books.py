# -*- coding: utf-8 -*-
import psycopg2
import requests
import xmltodict
import unidecode
import threading
import time
from datetime import datetime
import sys
from queue import Queue
from psycopg2.pool import ThreadedConnectionPool
# Local Files
from connect import connect
from config import config

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

AMAZON_SEARCH_URL = 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=REPLACE'


# TODO complete search_amazon_for_book()
def search_amazon_for_book(thread_id, book_title, book_author):
    '''
    Search amazon for the book by that author, grab the first link and return that url or None

    Returns string | None
    '''
    pass


# TODO complete fetch_new_book_info()
def fetch_new_book_info(thread_id, book_url):
    '''
    Returns {
        title: string,
        series: string | NONE,
        series_position: int | NONE,
        pages: int | NONE,
        publisher: string | NONE,
        orig_published_date: string | NONE,
        isbn10: string | NONE,
        isbn13: string | NONE,
        synopsis: string | NONE,
        amazon: {
            book_link: string,
            rating: decimal | NONE,
            synopsis: string | NONE,
            price: decimal | NONE,
        }
        authors: [string, ...], 
        categories: [string, ...], 
    } | None
    '''
    with print_lock:
        print(f'[Thread {thread_id}] Grabbing book from {book_url}')

    try:
        # TODO: create the parser
        return {}
    except Exception as error:
        with print_lock:
            print(f'[Thread {thread_id}] An Error occurred while trying to read from', book_url, error)
        return None


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

        book_author = book[0]
        book_title = book[1]

        with print_lock:
            print(f'[Thread {thread_id}] Working on task {book_title} by {book_author}')

        search_result = search_amazon_for_book(thread_id, book_title, book_author)

        if search_result:
            status = fetch_new_book_info(thread_id, search_result)

            # If the status is good, increase the number of books added
            if status:
                with shared_mutex:
                    count += 1

        book_queue.task_done()
        with print_lock:
            print(f'[Thread {thread_id}] Task Completed: {book_title}; Status: {status}')
        time.sleep(SLEEP_TIME)

    with print_lock:
        print(f'[Thread {thread_id}] Thread Ended')


def setup_db():
    global tcp
    # conn, cur = connect()
    params = config()
    tcp = ThreadedConnectionPool(1, 10, **params)

    print('[SETUP] TCP returned:', tcp)


def scrap_books():
    global tcp, count
    start = time.time()
    try:
        setup_db()

        for i in range(NUM_THREADS):
            t = threading.Thread(target=worker_thread, args=(i, ))
            # t.daemon = True
            t.start()

        # TODO read books from CSV file
        books_to_search = None

        # TODO: grab all books from the database

        # TODO: remove any books that have been already added OR mark them as to be updated

        if books_to_search != None:
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
