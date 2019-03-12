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
    date date NOT NULL
);

\unset ON_ERROR_STOP
