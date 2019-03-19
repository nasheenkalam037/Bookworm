\set ON_ERROR_STOP on
SET CLIENT_ENCODING TO 'utf8';
--
-- PostgreSQL database dump
--

CREATE SEQUENCE public."BookOfTheDay_idBookOfTheDay_sequence"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE TABLE public."BookOfTheDay" (
    "idBookOfTheDay" integer DEFAULT nextval('public."BookOfTheDay_idBookOfTheDay_sequence"'::regclass) NOT NULL,
    book_id integer NOT NULL,
    date timestamp with time zone NOT NULL
);

INSERT INTO public."BookOfTheDay" ("idBookOfTheDay", book_id, date) VALUES (1,315, '2019-03-17 19:52:24.119563-04');
INSERT INTO public."BookOfTheDay" ("idBookOfTheDay", book_id, date) VALUES (2,42, '2019-03-18 19:52:24.119563-04');
INSERT INTO public."BookOfTheDay" ("idBookOfTheDay", book_id, date) VALUES (3,83, '2019-03-19 19:52:24.119563-04');
INSERT INTO public."BookOfTheDay" ("idBookOfTheDay", book_id, date) VALUES (4,93, '2019-03-20 19:52:24.119563-04');
INSERT INTO public."BookOfTheDay" ("idBookOfTheDay", book_id, date) VALUES (5,364, '2019-03-21 19:52:24.119563-04');


\unset ON_ERROR_STOP
