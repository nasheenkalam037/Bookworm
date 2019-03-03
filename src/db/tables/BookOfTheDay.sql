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

--
-- TOC entry 3209 (class 1262 OID 19272)
-- Name: ece651; Type: DATABASE; Schema: -; Owner: s.n.azim
--

CREATE DATABASE ece651 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE ece651 OWNER TO "s.n.azim";

\connect ece651

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


ALTER TABLE public."BookOfTheDay" OWNER TO "s.n.azim";

--
-- TOC entry 3203 (class 0 OID 19293)
-- Dependencies: 202
-- Data for Name: BookOfTheDay; Type: TABLE DATA; Schema: public; Owner: s.n.azim
--



--
-- TOC entry 3079 (class 2606 OID 19405)
-- Name: BookOfTheDay BookOfTheDay_pkey; Type: CONSTRAINT; Schema: public; Owner: s.n.azim
--

ALTER TABLE ONLY public."BookOfTheDay"
    ADD CONSTRAINT "BookOfTheDay_pkey" PRIMARY KEY ("idBookOfTheDay");


--
-- TOC entry 3080 (class 2606 OID 19451)
-- Name: BookOfTheDay book_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: s.n.azim
--

ALTER TABLE ONLY public."BookOfTheDay"
    ADD CONSTRAINT book_id_fk FOREIGN KEY (book_id) REFERENCES public."Books"(book_id);


--
-- TOC entry 3210 (class 0 OID 0)
-- Dependencies: 202
-- Name: TABLE "BookOfTheDay"; Type: ACL; Schema: public; Owner: s.n.azim
--

GRANT ALL ON TABLE public."BookOfTheDay" TO ece651_ml;
GRANT ALL ON TABLE public."BookOfTheDay" TO ece651_web;
GRANT ALL ON TABLE public."BookOfTheDay" TO ece651_scraper;


-- Completed on 2019-03-03 10:30:43 EST

--
-- PostgreSQL database dump complete
--

