--
-- PostgreSQL database dump
--

-- Dumped from database version 11.1
-- Dumped by pg_dump version 11.1

-- Started on 2019-03-03 10:30:43 EST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 202 (class 1259 OID 19293)
-- Name: BookOfTheDay; Type: TABLE; Schema: public; Owner: s.n.azim
--

CREATE TABLE public."BookOfTheDay" (
    "idBookOfTheDay" integer DEFAULT nextval('public."BookOfTheDay_idBookOfTheDay_sequence"'::regclass) NOT NULL,
    book_id integer NOT NULL,
    date date NOT NULL
);