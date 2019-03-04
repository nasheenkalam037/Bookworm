
CREATE VIEW public."BookDetails" AS
 SELECT "Books".book_id,
    "Books".title,
    abb.author_id,
    abb.author_name,
    "Books".series,
    "Books".series_position,
    "Books".pages,
    "Books".publisher,
    "Books".orig_published_date,
    "Books".isbn10,
    "Books".isbn13,
    "Books".synopsis,
    ad.book_link AS amazon_link,
    ad.rating AS amazon_rating,
    ad.synopsis AS amazon_synopsis,
    ad.price AS amazon_price,
    ad.num_reviews AS amazon_num_reviews
   FROM ((public."Books"
     JOIN public."AmazonDetails" ad ON (("Books".book_id = ad.book_id)))
     LEFT JOIN ( SELECT DISTINCT ON (ab.book_id) a.author_id,
            ab.book_id,
            a.name AS author_name
           FROM (public."Author" a
             JOIN public."AuthorBooks" ab ON ((a.author_id = ab.author_id)))) abb ON (("Books".book_id = abb.book_id)));

