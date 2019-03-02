#!/usr/bin/env python3
import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from config import config

search_user_sql = '''
SELECT user_id FROM public."Users" 
	WHERE display_name = %(name)s  
'''

insert_user_sql = '''
INSERT INTO public."Users"(display_name, email, password_hash, created_from)
	VALUES (%(name)s, CONCAT(%(name)s, '@gmail.com'), ' ', 'Amazon')
    ON CONFLICT DO NOTHING
    RETURNING user_id
'''


def save_user(conn, review_info):
    try:
        cur = conn.cursor()
        for r in review_info:
            cur.execute(search_user_sql, r)
            
            if cur.statusmessage[7] != '0':
                user_id = cur.fetchone()[0]
            else:
                cur.execute(insert_user_sql, r)
                user_id = cur.fetchone()[0]

            save_review(conn, user_id, r)

        conn.commit()
    except Exception as err:
        print('Error Saving user:', err, review_info)

insert_review_sql = '''
INSERT INTO public."Reviews"(user_id, book_id, rating, review)
	VALUES (%s, %s, %s, %s)
'''


def save_review(conn, user_id, data):
    try:
        cur = conn.cursor()
        cur.execute(insert_review_sql, (user_id, data['book_id'], data['rating'], data['review']))
        conn.commit()
        
    except Exception as err:
        print('Error Saving review:', err, user_id)

if __name__ == "__main__":
    global tcp
    params = config()
    tcp = ThreadedConnectionPool(1, 10, **params)
    conn = tcp.getconn()
    review_info = [{'book_id': 24, 'user_id': 'AG3HZ5KORQIXZHUBLNMZNU35SCEA', 'name': 'fdddg', 'rating': 4.0, 'review': "This"}]

    save_user(conn, review_info)
    tcp.putconn(conn)