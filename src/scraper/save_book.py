#!/usr/bin/env python3

insert_book_sql = '''
INSERT INTO public."Books"(
	title, series, series_position, pages, publisher, orig_published_date, "isbn10", "isbn13", synopsis)
	VALUES (%(title)s, %(series)s, %(series_position)s, %(pages)s, %(publisher)s, %(orig_published_date)s, 
    %(isbn10)s, %(isbn13)s, %(synopsis)s)
    ON CONFLICT("isbn13") DO UPDATE SET title=EXCLUDED.title
    RETURNING book_id
'''


def save_book(conn, book):
    try:
        cur = conn.cursor()
        cur.execute(insert_book_sql, book)
        book_id = cur.fetchone()[0]
        conn.commit()

        save_categories(conn, book_id, book)
        save_authors(conn, book_id, book)
        save_amazon_details(conn, book_id, book)
    except Exception as err:
        print('Error Saving book:', err, book)


insert_cat_sql = '''
INSERT INTO public."Categories"("name")
	VALUES (%s)
    ON CONFLICT("name") DO UPDATE SET name=EXCLUDED.name
	RETURNING categories_id
'''
insert_bookcat_sql = '''
INSERT INTO public."BookCategories"(
	book_id, category_id)
	VALUES (%s, %s)
    ON CONFLICT DO NOTHING
'''


def save_categories(conn, book_id, book):
    cur = conn.cursor()
    # Insert all new categories
    categories = {}
    for c in book['categories']:
        cur.execute(insert_cat_sql, (c, ))
        cat_id = cur.fetchone()[0]
        categories[c] = cat_id

    # Link book to each category
    for c_name, c_id in categories.items():
        cur.execute(insert_bookcat_sql, (book_id, c_id))

    # Commit
    conn.commit()


insert_author_sql = '''
INSERT INTO public."Author"("name")
	VALUES (%s)
    ON CONFLICT("name") DO UPDATE SET name=EXCLUDED.name
	RETURNING author_id
'''
insert_bookauthor_sql = '''
INSERT INTO public."AuthorBooks"(
	book_id, author_id)
	VALUES (%s, %s)
    ON CONFLICT DO NOTHING
'''


def save_authors(conn, book_id, book):
    cur = conn.cursor()
    # Insert all new authors
    authors = {}
    for c in book['authors']:
        cur.execute(insert_author_sql, (c, ))
        author_id = cur.fetchone()[0]
        authors[c] = author_id

    # Link book to each author
    for a_name, a_id in authors.items():
        cur.execute(insert_bookauthor_sql, (book_id, a_id))

    # Commit
    conn.commit()


insert_amazon_sql = '''
INSERT INTO public."AmazonDetails"(
	book_id, book_link, rating, num_reviews, synopsis, price)
	VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT("book_id") DO UPDATE SET 
    book_link=EXCLUDED.book_link,
    rating=EXCLUDED.rating,
    num_reviews=EXCLUDED.num_reviews,
    synopsis=EXCLUDED.synopsis,
    price=EXCLUDED.price
'''


def save_amazon_details(conn, book_id, book):
    cur = conn.cursor()
    az = book['amazon']
    cur.execute(insert_amazon_sql,
                (book_id, az['book_link'], az['rating'], az['num_reviews'], az['synopsis'], az['price']))
    conn.commit()