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
import get_amazon_review_info as getReviewInfo
import get_book_information as getBookInfo
from save_review import save_user
from save_book import save_book
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

def get_users_books(thread_id, book, user_books, review_info):
    for r in review_info:
        book_id = r['book_id']
        user_id = r['user_id']                
        if user_id in user_books:
            user_books[user_id].append(book_id)
        else:
            user_books[user_id] = [book_id]

    for user in user_books: #Find more Books by the Users we already have
        search_result = getReviewInfo.fetch_review_from_user_acc(thread_id, book, user)

        if search_result:
            for result in search_result:
                if result['book_id_link'] is not int:
                    book_info = getBookInfo.fetch_new_book_info(thread_id, result['book_id_link'])

                    # If the book_info is good, increase the number of books added
                    if book_info:
                        conn = tcp.getconn()
                        book_id = save_book(conn, book_info)
                        tcp.putconn(conn)
                        
                        print("book_id: ", book_id)
                        
                        result['book_id_link'] = book_id
                        user_books[user].append(result['book_id_link'])
                        review_info.append(result)

    good_users = {}
    for user in user_books: # Remove all Users with only 1 Book
        if len(user_books[user]) > 1:
            good_users[user] = user_books[user]
    
    book_users = {}
    for user in good_users:
        for book in good_users[user]:
            if book in book_users:
                book_users[book].append(user)
            else:  
                book_users[book] = [user]
    
    good_books = {}
    for book in book_users: # Remove all Books with only 1 User
        if len(book_users[book]) > 1:
            good_books[book] = book_users[book]

    good_reviews = []
    for review in review_info:
        if review['user_id'] in good_users:# Remove Reviews of Users with only 1 book review 
            good_reviews.append(review)
        else:
            if review['book_id'] in good_books:# Remove Reviews on Books with only 1 user review
                good_reviews.append(review)

    return good_reviews

def worker_thread(thread_id, user_books, good_users, good_books):
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

        review_info = getReviewInfo.fetch_review_data(thread_id, book)
        
        if review_info:
            good_reviews = get_users_books(thread_id, book, user_books, review_info)
            
            print("Good-Review: ", good_reviews)
            conn = tcp.getconn()
            save_user(conn, good_reviews)
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

        user_books = {}
        good_users = {}
        good_books = {}
        for i in range(NUM_THREADS):
            t = threading.Thread(target=worker_thread, args=(i, user_books, good_users, good_books))
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