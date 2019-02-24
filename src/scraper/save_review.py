#!/usr/bin/env python3

insert_review_sql = '''
INSERT INTO public."Reviews"(
	review_id, user_id, rating, review)
	VALUES (%(review_id)s, %(amazon_user_id)s, %(rating)s, %(review)s)
'''


def save_review(conn, review):
    try:
        cur = conn.cursor()
        cur.execute(insert_review_sql, review)
        cur.fetchone()[0]
        conn.commit()
    except Exception as err:
        print('Error Saving review:', err, review)