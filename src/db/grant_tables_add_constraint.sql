-- TODO: add all CREATE SEQUENCE statements here


--- Books

ALTER TABLE ONLY public."Books"
    ADD CONSTRAINT "Books_pkey" PRIMARY KEY (book_id);


ALTER TABLE ONLY public."Books"
    ADD CONSTRAINT unique_isbn10 UNIQUE (isbn10);


ALTER TABLE ONLY public."Books"
    ADD CONSTRAINT unique_isbn13 UNIQUE (isbn13);


GRANT ALL ON TABLE public."Books" TO ece651_ml;
GRANT ALL ON TABLE public."Books" TO ece651_web;
GRANT ALL ON TABLE public."Books" TO ece651_scraper;

--- Author

ALTER TABLE ONLY public."Author"
    ADD CONSTRAINT "Author_pkey" PRIMARY KEY (author_id);


ALTER TABLE ONLY public."Author"
    ADD CONSTRAINT unique_author_name UNIQUE (name);


GRANT ALL ON TABLE public."Author" TO ece651_ml;
GRANT ALL ON TABLE public."Author" TO ece651_web;
GRANT ALL ON TABLE public."Author" TO ece651_scraper;

--- AuthorBooks

ALTER TABLE ONLY public."AuthorBooks"
    ADD CONSTRAINT "AuthorBooks_pkey" PRIMARY KEY (author_id, book_id);


ALTER TABLE ONLY public."AuthorBooks"
    ADD CONSTRAINT author_id_fk FOREIGN KEY (author_id) REFERENCES public."Author"(author_id);


ALTER TABLE ONLY public."AuthorBooks"
    ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES public."Books"(book_id);


GRANT ALL ON TABLE public."AuthorBooks" TO ece651_ml;
GRANT ALL ON TABLE public."AuthorBooks" TO ece651_web;
GRANT ALL ON TABLE public."AuthorBooks" TO ece651_scraper;

--- Categories

ALTER TABLE ONLY public."Categories"
    ADD CONSTRAINT "Categories_pkey" PRIMARY KEY (categories_id);


ALTER TABLE ONLY public."Categories"
    ADD CONSTRAINT unique_cat_name UNIQUE (name);


GRANT ALL ON TABLE public."Categories" TO ece651_ml;
GRANT ALL ON TABLE public."Categories" TO ece651_web;
GRANT ALL ON TABLE public."Categories" TO ece651_scraper;

--- BookCategories

ALTER TABLE ONLY public."BookCategories"
    ADD CONSTRAINT "Book_Category_pkey" PRIMARY KEY (book_id, category_id);


ALTER TABLE ONLY public."BookCategories"
    ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES public."Books"(book_id);


ALTER TABLE ONLY public."BookCategories"
    ADD CONSTRAINT category_id_fk FOREIGN KEY (category_id) REFERENCES public."Categories"(categories_id);


GRANT ALL ON TABLE public."BookCategories" TO ece651_ml;
GRANT ALL ON TABLE public."BookCategories" TO ece651_web;
GRANT ALL ON TABLE public."BookCategories" TO ece651_scraper;

--- BookOfTheDay

ALTER TABLE ONLY public."BookOfTheDay"
    ADD CONSTRAINT "BookOfTheDay_pkey" PRIMARY KEY ("idBookOfTheDay");


ALTER TABLE ONLY public."BookOfTheDay"
    ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES public."Books"(book_id);


GRANT ALL ON TABLE public."BookOfTheDay" TO ece651_ml;
GRANT ALL ON TABLE public."BookOfTheDay" TO ece651_web;
GRANT ALL ON TABLE public."BookOfTheDay" TO ece651_scraper;

--- AmazonDetails

ALTER TABLE ONLY public."AmazonDetails"
    ADD CONSTRAINT "AmazonDetails_pkey" PRIMARY KEY (book_id);


ALTER TABLE ONLY public."AmazonDetails"
    ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES public."Books"(book_id);


GRANT ALL ON TABLE public."AmazonDetails" TO ece651_ml;
GRANT ALL ON TABLE public."AmazonDetails" TO ece651_web;
GRANT ALL ON TABLE public."AmazonDetails" TO ece651_scraper;

--- Users

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (user_id);


ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT unique_email UNIQUE (email);


GRANT ALL ON TABLE public."Users" TO ece651_ml;
GRANT ALL ON TABLE public."Users" TO ece651_web;
GRANT ALL ON TABLE public."Users" TO ece651_scraper;

--- Reviews

ALTER TABLE ONLY public."Reviews"
    ADD CONSTRAINT "Reviews_pkey" PRIMARY KEY (review_id);


ALTER TABLE ONLY public."Reviews"
    ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES public."Books"(book_id);


ALTER TABLE ONLY public."Reviews"
    ADD CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES public."Users"(user_id);


GRANT ALL ON TABLE public."Reviews" TO ece651_ml;
GRANT ALL ON TABLE public."Reviews" TO ece651_web;
GRANT ALL ON TABLE public."Reviews" TO ece651_scraper;