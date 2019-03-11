--
-- PostgreSQL database dump
--

CREATE TABLE public."BookOfTheDay" (
    "idBookOfTheDay" integer DEFAULT nextval('public."BookOfTheDay_idBookOfTheDay_sequence"'::regclass) NOT NULL,
    book_id integer NOT NULL,
    date date NOT NULL
);