--
-- PostgreSQL database dump
--

-- Dumped from database version 11.1
-- Dumped by pg_dump version 11.1

-- Started on 2019-03-03 10:24:46 EST

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
-- TOC entry 3210 (class 1262 OID 19272)
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
-- TOC entry 198 (class 1259 OID 19281)
-- Name: Author; Type: TABLE; Schema: public; Owner: s.n.azim
--

CREATE TABLE public."Author" (
    author_id integer DEFAULT nextval('public."Author_author_id_sequence"'::regclass) NOT NULL,
    name character varying(200) NOT NULL
);


ALTER TABLE public."Author" OWNER TO "s.n.azim";

--
-- TOC entry 3204 (class 0 OID 19281)
-- Dependencies: 198
-- Data for Name: Author; Type: TABLE DATA; Schema: public; Owner: s.n.azim
--

INSERT INTO public."Author" (author_id, name) VALUES (70, 'Thomas G. West');
INSERT INTO public."Author" (author_id, name) VALUES (99, 'John Galt');
INSERT INTO public."Author" (author_id, name) VALUES (100, 'Henk Tijms');
INSERT INTO public."Author" (author_id, name) VALUES (104, 'Katrin Becker');
INSERT INTO public."Author" (author_id, name) VALUES (105, 'Melanie Becker');
INSERT INTO public."Author" (author_id, name) VALUES (106, 'John H. Schwarz');
INSERT INTO public."Author" (author_id, name) VALUES (107, 'Arthur Golden');
INSERT INTO public."Author" (author_id, name) VALUES (103, 'Leo Tolstoy');
INSERT INTO public."Author" (author_id, name) VALUES (111, 'Timothy Gowers');
INSERT INTO public."Author" (author_id, name) VALUES (112, 'June Barrow-Green');
INSERT INTO public."Author" (author_id, name) VALUES (113, 'Imre Leader');
INSERT INTO public."Author" (author_id, name) VALUES (116, 'R. Douglas Gregory');
INSERT INTO public."Author" (author_id, name) VALUES (221, 'J.D. Salinger');
INSERT INTO public."Author" (author_id, name) VALUES (189, 'John Cleland');
INSERT INTO public."Author" (author_id, name) VALUES (262, 'David A. B. Miller');
INSERT INTO public."Author" (author_id, name) VALUES (37, 'Plato');
INSERT INTO public."Author" (author_id, name) VALUES (36, 'Eric S. Raymond');
INSERT INTO public."Author" (author_id, name) VALUES (79, 'Don Adams');
INSERT INTO public."Author" (author_id, name) VALUES (75, 'W. R. M. Lamb');
INSERT INTO public."Author" (author_id, name) VALUES (101, 'Sir John Barrow');
INSERT INTO public."Author" (author_id, name) VALUES (95, 'Ken Follett');
INSERT INTO public."Author" (author_id, name) VALUES (71, 'Grace Starry West');
INSERT INTO public."Author" (author_id, name) VALUES (73, 'Joe Sachs');
INSERT INTO public."Author" (author_id, name) VALUES (134, 'Oscar Wilde');
INSERT INTO public."Author" (author_id, name) VALUES (135, 'Peter Raby');
INSERT INTO public."Author" (author_id, name) VALUES (89, 'F. Scott Fitzgerald');
INSERT INTO public."Author" (author_id, name) VALUES (228, 'Nevil Shute');
INSERT INTO public."Author" (author_id, name) VALUES (210, 'George Orwell');
INSERT INTO public."Author" (author_id, name) VALUES (136, 'Gary Schmidgall');
INSERT INTO public."Author" (author_id, name) VALUES (229, 'Jenny Colgan');
INSERT INTO public."Author" (author_id, name) VALUES (230, 'Alexandre Dumas');
INSERT INTO public."Author" (author_id, name) VALUES (231, 'Peter Washington');
INSERT INTO public."Author" (author_id, name) VALUES (232, 'Umberto Eco');
INSERT INTO public."Author" (author_id, name) VALUES (233, 'Upton Sinclair');
INSERT INTO public."Author" (author_id, name) VALUES (234, 'Johanna Spyri');
INSERT INTO public."Author" (author_id, name) VALUES (266, 'Dr Kevin Houston');
INSERT INTO public."Author" (author_id, name) VALUES (152, 'Richard Adams');
INSERT INTO public."Author" (author_id, name) VALUES (153, 'Louisa May Alcott');
INSERT INTO public."Author" (author_id, name) VALUES (235, 'Gabriel Garcia Marquez');
INSERT INTO public."Author" (author_id, name) VALUES (155, 'Aldous Huxley');
INSERT INTO public."Author" (author_id, name) VALUES (157, 'Jeffrey Archer');
INSERT INTO public."Author" (author_id, name) VALUES (158, 'Melanie Mitchell');
INSERT INTO public."Author" (author_id, name) VALUES (159, 'John Irving');
INSERT INTO public."Author" (author_id, name) VALUES (160, 'Oliver Johns');
INSERT INTO public."Author" (author_id, name) VALUES (168, 'Franz Kafka');
INSERT INTO public."Author" (author_id, name) VALUES (239, 'John Steinbeck');
INSERT INTO public."Author" (author_id, name) VALUES (175, 'Charlotte Bronte');
INSERT INTO public."Author" (author_id, name) VALUES (177, 'L. Frank Baum');
INSERT INTO public."Author" (author_id, name) VALUES (178, 'Arthur Pober Ed.D');
INSERT INTO public."Author" (author_id, name) VALUES (179, 'Scott McKowen');
INSERT INTO public."Author" (author_id, name) VALUES (180, 'Rudyard Kipling');
INSERT INTO public."Author" (author_id, name) VALUES (181, 'Emily Bronte');
INSERT INTO public."Author" (author_id, name) VALUES (182, 'Juliet Barker');
INSERT INTO public."Author" (author_id, name) VALUES (183, 'Alice Hoffman');
INSERT INTO public."Author" (author_id, name) VALUES (141, 'George R. R. Martin');
INSERT INTO public."Author" (author_id, name) VALUES (186, 'Harper Lee');
INSERT INTO public."Author" (author_id, name) VALUES (191, 'Miguel de Cervantes');
INSERT INTO public."Author" (author_id, name) VALUES (192, 'Edith Grossman');
INSERT INTO public."Author" (author_id, name) VALUES (194, 'Gareth James');
INSERT INTO public."Author" (author_id, name) VALUES (195, 'Daniela Witten');
INSERT INTO public."Author" (author_id, name) VALUES (196, 'Trevor Hastie');
INSERT INTO public."Author" (author_id, name) VALUES (197, 'Robert Tibshirani');
INSERT INTO public."Author" (author_id, name) VALUES (201, 'Colleen McCullough');
INSERT INTO public."Author" (author_id, name) VALUES (202, 'Wilkie Collins');
INSERT INTO public."Author" (author_id, name) VALUES (203, 'Herman Melville');
INSERT INTO public."Author" (author_id, name) VALUES (205, 'Karen C. Fox');
INSERT INTO public."Author" (author_id, name) VALUES (206, 'Stan Gibilisco');
INSERT INTO public."Author" (author_id, name) VALUES (212, 'Sir William Golding');
INSERT INTO public."Author" (author_id, name) VALUES (213, 'E M Forster');
INSERT INTO public."Author" (author_id, name) VALUES (215, 'Nathaniel Hawthorne');
INSERT INTO public."Author" (author_id, name) VALUES (236, 'George Eliot');
INSERT INTO public."Author" (author_id, name) VALUES (217, 'Charles Dickens');
INSERT INTO public."Author" (author_id, name) VALUES (19, 'Nietzsche');
INSERT INTO public."Author" (author_id, name) VALUES (240, 'Gabriel Garc-a M-rquez');
INSERT INTO public."Author" (author_id, name) VALUES (249, 'James L. Meriam');
INSERT INTO public."Author" (author_id, name) VALUES (255, 'Honore de Balzac');
INSERT INTO public."Author" (author_id, name) VALUES (256, 'Andronum');
INSERT INTO public."Author" (author_id, name) VALUES (257, 'Katharine Prescott Wormeley');
INSERT INTO public."Author" (author_id, name) VALUES (263, 'Michael T. Vaughn');
INSERT INTO public."Author" (author_id, name) VALUES (149, 'Douglas Adams');
INSERT INTO public."Author" (author_id, name) VALUES (187, 'Gaston Leroux');
INSERT INTO public."Author" (author_id, name) VALUES (23, 'James Joyce');
INSERT INTO public."Author" (author_id, name) VALUES (24, 'Cedric Watts');
INSERT INTO public."Author" (author_id, name) VALUES (83, 'Xenophon');
INSERT INTO public."Author" (author_id, name) VALUES (44, 'Cornelius Ladd Kitchel');
INSERT INTO public."Author" (author_id, name) VALUES (46, 'C. S. Lewis');
INSERT INTO public."Author" (author_id, name) VALUES (47, 'Pauline Baynes');
INSERT INTO public."Author" (author_id, name) VALUES (102, 'Dan Abnett');
INSERT INTO public."Author" (author_id, name) VALUES (109, 'James Stewart');
INSERT INTO public."Author" (author_id, name) VALUES (92, 'Bram Stoker');
INSERT INTO public."Author" (author_id, name) VALUES (114, 'Robert Tressell');
INSERT INTO public."Author" (author_id, name) VALUES (97, 'Neil Gaiman');
INSERT INTO public."Author" (author_id, name) VALUES (190, 'Michael Crichton');
INSERT INTO public."Author" (author_id, name) VALUES (115, 'J. R. R Tolkien');
INSERT INTO public."Author" (author_id, name) VALUES (122, 'Sun Tzu');
INSERT INTO public."Author" (author_id, name) VALUES (96, 'C S Lewis');
INSERT INTO public."Author" (author_id, name) VALUES (124, 'Thomas Hardy');
INSERT INTO public."Author" (author_id, name) VALUES (125, 'Jules Verne');
INSERT INTO public."Author" (author_id, name) VALUES (261, 'Kate Macdonald');
INSERT INTO public."Author" (author_id, name) VALUES (176, 'Stephen King');
INSERT INTO public."Author" (author_id, name) VALUES (118, 'International Conference on Computation of Differential Equations and');
INSERT INTO public."Author" (author_id, name) VALUES (318, 'Nick Kyme');
INSERT INTO public."Author" (author_id, name) VALUES (265, 'Sir Arthur Conan Doyle');
INSERT INTO public."Author" (author_id, name) VALUES (150, 'Brian Cox');
INSERT INTO public."Author" (author_id, name) VALUES (151, 'Jeff Forshaw');
INSERT INTO public."Author" (author_id, name) VALUES (156, 'Steven Holzner');
INSERT INTO public."Author" (author_id, name) VALUES (161, 'Moshe Sipper');
INSERT INTO public."Author" (author_id, name) VALUES (316, 'David Annandale');
INSERT INTO public."Author" (author_id, name) VALUES (163, 'Henry James');
INSERT INTO public."Author" (author_id, name) VALUES (164, 'Rex E. Bradford');
INSERT INTO public."Author" (author_id, name) VALUES (166, 'Paul Morneau');
INSERT INTO public."Author" (author_id, name) VALUES (21, 'William Shakespeare');
INSERT INTO public."Author" (author_id, name) VALUES (171, 'Dr. Barbara A. Mowat');
INSERT INTO public."Author" (author_id, name) VALUES (173, 'Louis de Bernieres');
INSERT INTO public."Author" (author_id, name) VALUES (184, 'Jon Erickson');
INSERT INTO public."Author" (author_id, name) VALUES (127, 'Philip Pullman');
INSERT INTO public."Author" (author_id, name) VALUES (130, 'Lucy Hughes-Hallett');
INSERT INTO public."Author" (author_id, name) VALUES (193, 'Daphne du Maurier');
INSERT INTO public."Author" (author_id, name) VALUES (146, 'Ashok Das');
INSERT INTO public."Author" (author_id, name) VALUES (188, 'Michelle Magorian');
INSERT INTO public."Author" (author_id, name) VALUES (198, 'Eoin Colfer');
INSERT INTO public."Author" (author_id, name) VALUES (204, 'Gustave Flaubert');
INSERT INTO public."Author" (author_id, name) VALUES (207, 'Joseph Conrad');
INSERT INTO public."Author" (author_id, name) VALUES (214, 'Holt Rinehart and Winston');
INSERT INTO public."Author" (author_id, name) VALUES (199, 'Michael Moreci');
INSERT INTO public."Author" (author_id, name) VALUES (200, 'Stephen Gilpin');
INSERT INTO public."Author" (author_id, name) VALUES (98, 'Terry Pratchett');
INSERT INTO public."Author" (author_id, name) VALUES (119, 'Kang Feng');
INSERT INTO public."Author" (author_id, name) VALUES (208, 'Jacques Berthoud');
INSERT INTO public."Author" (author_id, name) VALUES (209, 'Mara Kalnins');
INSERT INTO public."Author" (author_id, name) VALUES (219, 'Salman Rushdie');
INSERT INTO public."Author" (author_id, name) VALUES (211, 'Ann Patchett');
INSERT INTO public."Author" (author_id, name) VALUES (128, 'Ernest Hemingway');
INSERT INTO public."Author" (author_id, name) VALUES (224, 'Patrick Hemingway');
INSERT INTO public."Author" (author_id, name) VALUES (241, 'Robert Louis Stevenson');
INSERT INTO public."Author" (author_id, name) VALUES (244, 'Arvind Bhatnagar');
INSERT INTO public."Author" (author_id, name) VALUES (237, 'Lynne Sharon Schwartz');
INSERT INTO public."Author" (author_id, name) VALUES (238, 'Megan McDaniel');
INSERT INTO public."Author" (author_id, name) VALUES (245, 'William Livingston');
INSERT INTO public."Author" (author_id, name) VALUES (250, 'L. G. Kraige');
INSERT INTO public."Author" (author_id, name) VALUES (253, 'Karl F. Kuhn');
INSERT INTO public."Author" (author_id, name) VALUES (137, 'J.K. Rowling');
INSERT INTO public."Author" (author_id, name) VALUES (251, 'J. N. Bolton');
INSERT INTO public."Author" (author_id, name) VALUES (20, 'Friedrich Wilhelm Nietzsche');
INSERT INTO public."Author" (author_id, name) VALUES (147, 'Thomas Ferbel');
INSERT INTO public."Author" (author_id, name) VALUES (94, 'Tudor Humphries');
INSERT INTO public."Author" (author_id, name) VALUES (172, 'Paul Werstine Ph.D.');
INSERT INTO public."Author" (author_id, name) VALUES (367, 'James DeFranza');
INSERT INTO public."Author" (author_id, name) VALUES (368, 'Daniel Gagliardi');
INSERT INTO public."Author" (author_id, name) VALUES (569, 'J. R. R. Tolkien');
INSERT INTO public."Author" (author_id, name) VALUES (571, 'Stephen Hawking');
INSERT INTO public."Author" (author_id, name) VALUES (417, 'Madeleine L''Engle');
INSERT INTO public."Author" (author_id, name) VALUES (414, 'Carol Ellison');
INSERT INTO public."Author" (author_id, name) VALUES (429, 'J M Kennedy');
INSERT INTO public."Author" (author_id, name) VALUES (576, 'CARD ORSON SCOTT');
INSERT INTO public."Author" (author_id, name) VALUES (432, 'Anthony Ludovici');
INSERT INTO public."Author" (author_id, name) VALUES (578, 'Charles Vess');
INSERT INTO public."Author" (author_id, name) VALUES (444, 'Thomas Hobbes');
INSERT INTO public."Author" (author_id, name) VALUES (447, 'Nicolo Machiavelli');
INSERT INTO public."Author" (author_id, name) VALUES (446, 'Leslie Stephen');
INSERT INTO public."Author" (author_id, name) VALUES (450, 'Ludwig Wittgenstein');
INSERT INTO public."Author" (author_id, name) VALUES (445, 'Bertrand Russell');
INSERT INTO public."Author" (author_id, name) VALUES (453, 'Tom Robinson');
INSERT INTO public."Author" (author_id, name) VALUES (452, 'J F Marques Pereira');
INSERT INTO public."Author" (author_id, name) VALUES (455, 'Ben Jeapes');
INSERT INTO public."Author" (author_id, name) VALUES (456, 'Dustin Brady');
INSERT INTO public."Author" (author_id, name) VALUES (457, 'Jesse Brady');
INSERT INTO public."Author" (author_id, name) VALUES (580, 'George Toufexis');
INSERT INTO public."Author" (author_id, name) VALUES (460, 'Jan Berenstain');
INSERT INTO public."Author" (author_id, name) VALUES (461, 'Mike Berenstain');
INSERT INTO public."Author" (author_id, name) VALUES (594, 'Neal Stephenson');
INSERT INTO public."Author" (author_id, name) VALUES (584, 'Krasimir Tsonev');
INSERT INTO public."Author" (author_id, name) VALUES (476, 'Greg Bear');
INSERT INTO public."Author" (author_id, name) VALUES (485, 'Edgar Rice Burroughs');
INSERT INTO public."Author" (author_id, name) VALUES (468, 'Robert Venditti');
INSERT INTO public."Author" (author_id, name) VALUES (475, 'Paul Thagard');
INSERT INTO public."Author" (author_id, name) VALUES (585, 'Ann Leckie');
INSERT INTO public."Author" (author_id, name) VALUES (586, 'Marko Kloos');
INSERT INTO public."Author" (author_id, name) VALUES (557, 'Lemony Snicket');
INSERT INTO public."Author" (author_id, name) VALUES (494, 'Bill Siekiewicz');
INSERT INTO public."Author" (author_id, name) VALUES (495, 'Guillermo Del Toro');
INSERT INTO public."Author" (author_id, name) VALUES (493, 'H.G. Wells');
INSERT INTO public."Author" (author_id, name) VALUES (497, 'Bernard Mayes');
INSERT INTO public."Author" (author_id, name) VALUES (500, 'Leslie Valiant');
INSERT INTO public."Author" (author_id, name) VALUES (593, 'John Ringo');
INSERT INTO public."Author" (author_id, name) VALUES (440, 'John Stuart Mill');
INSERT INTO public."Author" (author_id, name) VALUES (505, 'Walter Kaufmann');
INSERT INTO public."Author" (author_id, name) VALUES (507, 'Joseph Staten');
INSERT INTO public."Author" (author_id, name) VALUES (510, 'Dave McKenan');
INSERT INTO public."Author" (author_id, name) VALUES (513, 'D Holland');
INSERT INTO public."Author" (author_id, name) VALUES (566, 'Isaac Asimov');
INSERT INTO public."Author" (author_id, name) VALUES (512, 'James Dashner');
INSERT INTO public."Author" (author_id, name) VALUES (595, 'Peter Clines');
INSERT INTO public."Author" (author_id, name) VALUES (596, 'Kim Stanley Robinson');
INSERT INTO public."Author" (author_id, name) VALUES (583, 'John Scalzi');
INSERT INTO public."Author" (author_id, name) VALUES (521, 'Richard Herman');
INSERT INTO public."Author" (author_id, name) VALUES (121, 'Zhong-Ci Shi');
INSERT INTO public."Author" (author_id, name) VALUES (532, 'Neil Jones');
INSERT INTO public."Author" (author_id, name) VALUES (533, 'David Pringle');
INSERT INTO public."Author" (author_id, name) VALUES (389, 'Graham McNeill');
INSERT INTO public."Author" (author_id, name) VALUES (328, 'Lindsey Priestley');
INSERT INTO public."Author" (author_id, name) VALUES (712, 'Andy Lanning');
INSERT INTO public."Author" (author_id, name) VALUES (541, 'Robertson Davies');
INSERT INTO public."Author" (author_id, name) VALUES (469, 'Orpheus Collar');
INSERT INTO public."Author" (author_id, name) VALUES (527, 'Nicci French');
INSERT INTO public."Author" (author_id, name) VALUES (478, 'Chuck Palahniuk');
INSERT INTO public."Author" (author_id, name) VALUES (488, 'William C. Dietz');
INSERT INTO public."Author" (author_id, name) VALUES (672, 'Alastair Batchelor');
INSERT INTO public."Author" (author_id, name) VALUES (565, 'Dean White');
INSERT INTO public."Author" (author_id, name) VALUES (534, 'Marc Gascoigne');
INSERT INTO public."Author" (author_id, name) VALUES (535, 'Christian Dunn');
INSERT INTO public."Author" (author_id, name) VALUES (608, 'Robert Moore');
INSERT INTO public."Author" (author_id, name) VALUES (609, 'Doug Gillette');
INSERT INTO public."Author" (author_id, name) VALUES (610, 'Mario Puzo');
INSERT INTO public."Author" (author_id, name) VALUES (616, 'Joseph L. Heller');
INSERT INTO public."Author" (author_id, name) VALUES (613, 'Richard Matheson');
INSERT INTO public."Author" (author_id, name) VALUES (614, 'Bruce Bueno de Mesquita');
INSERT INTO public."Author" (author_id, name) VALUES (615, 'Alastair Smith');
INSERT INTO public."Author" (author_id, name) VALUES (619, 'Richard Preston');
INSERT INTO public."Author" (author_id, name) VALUES (623, 'Dave Eggers');
INSERT INTO public."Author" (author_id, name) VALUES (638, 'Lee Harrington');
INSERT INTO public."Author" (author_id, name) VALUES (639, 'RiggerJay');
INSERT INTO public."Author" (author_id, name) VALUES (628, 'R. E. McDermott');
INSERT INTO public."Author" (author_id, name) VALUES (587, 'Ramez Naam');
INSERT INTO public."Author" (author_id, name) VALUES (598, 'Evan Currie');
INSERT INTO public."Author" (author_id, name) VALUES (591, 'Pierce Brown');
INSERT INTO public."Author" (author_id, name) VALUES (673, 'James K. Rollins');
INSERT INTO public."Author" (author_id, name) VALUES (644, 'Lee Child New York Times Bestselling Author');
INSERT INTO public."Author" (author_id, name) VALUES (674, 'David Hartman');
INSERT INTO public."Author" (author_id, name) VALUES (663, 'James S. A. Corey');
INSERT INTO public."Author" (author_id, name) VALUES (486, 'Joe Hill');
INSERT INTO public."Author" (author_id, name) VALUES (662, 'Mike Brooks');
INSERT INTO public."Author" (author_id, name) VALUES (84, 'Nicholas Denyer');
INSERT INTO public."Author" (author_id, name) VALUES (359, 'Paul and Brenda Neal');
INSERT INTO public."Author" (author_id, name) VALUES (589, 'Chester Gould');
INSERT INTO public."Author" (author_id, name) VALUES (676, 'Eva Leon');
INSERT INTO public."Author" (author_id, name) VALUES (464, 'Rick Riordan');
INSERT INTO public."Author" (author_id, name) VALUES (120, 'Chung-Tzu Shih');
INSERT INTO public."Author" (author_id, name) VALUES (713, 'Olivier Coipel');
INSERT INTO public."Author" (author_id, name) VALUES (343, 'J.K.Rowling');
INSERT INTO public."Author" (author_id, name) VALUES (536, 'Ian Watson');
INSERT INTO public."Author" (author_id, name) VALUES (415, 'Frederick Mosteller');
INSERT INTO public."Author" (author_id, name) VALUES (393, 'Gav Thorpe');
INSERT INTO public."Author" (author_id, name) VALUES (225, 'Sean Hemingway');
INSERT INTO public."Author" (author_id, name) VALUES (770, 'Rosemary Ashton');
INSERT INTO public."Author" (author_id, name) VALUES (499, 'Aaron Dembski-Bowden');
INSERT INTO public."Author" (author_id, name) VALUES (743, 'Ben Counter');
INSERT INTO public."Author" (author_id, name) VALUES (648, 'Trevor Noah');
INSERT INTO public."Author" (author_id, name) VALUES (782, 'Mike Lee');
INSERT INTO public."Author" (author_id, name) VALUES (416, 'Hossein Pishro-Nik');
INSERT INTO public."Author" (author_id, name) VALUES (459, 'David G. Myers');
INSERT INTO public."Author" (author_id, name) VALUES (423, 'Scott Brick');
INSERT INTO public."Author" (author_id, name) VALUES (424, 'Gabrielle De Cuir');
INSERT INTO public."Author" (author_id, name) VALUES (418, 'Leonard S. Marcus');
INSERT INTO public."Author" (author_id, name) VALUES (433, 'Adrian Collins');
INSERT INTO public."Author" (author_id, name) VALUES (502, 'Eric Nylund');
INSERT INTO public."Author" (author_id, name) VALUES (435, 'Paul Reitter');
INSERT INTO public."Author" (author_id, name) VALUES (436, 'Chad Wellmon');
INSERT INTO public."Author" (author_id, name) VALUES (437, 'Damion Searls');
INSERT INTO public."Author" (author_id, name) VALUES (816, 'H. L. Mencken');
INSERT INTO public."Author" (author_id, name) VALUES (357, 'James Swallow');
INSERT INTO public."Author" (author_id, name) VALUES (443, 'Rene Descartes');
INSERT INTO public."Author" (author_id, name) VALUES (822, 'John Veitch');
INSERT INTO public."Author" (author_id, name) VALUES (824, 'Lois Lowry');
INSERT INTO public."Author" (author_id, name) VALUES (832, 'NOFX');
INSERT INTO public."Author" (author_id, name) VALUES (833, 'Jeff Alulis');
INSERT INTO public."Author" (author_id, name) VALUES (462, 'Niccolo Machiavelli');
INSERT INTO public."Author" (author_id, name) VALUES (463, 'Constantin Vaughn');
INSERT INTO public."Author" (author_id, name) VALUES (588, 'Joshua Dalzelle');
INSERT INTO public."Author" (author_id, name) VALUES (487, 'Charles Paul Wilson III');
INSERT INTO public."Author" (author_id, name) VALUES (839, 'Jose Villarrubia');
INSERT INTO public."Author" (author_id, name) VALUES (838, 'Attila Futaki');
INSERT INTO public."Author" (author_id, name) VALUES (492, 'H. G. Wells');
INSERT INTO public."Author" (author_id, name) VALUES (501, 'Tim Lebbon');
INSERT INTO public."Author" (author_id, name) VALUES (434, 'Friedrich Nietzsche');
INSERT INTO public."Author" (author_id, name) VALUES (508, 'Tobias S. Buckell');
INSERT INTO public."Author" (author_id, name) VALUES (511, 'Karen Traviss');
INSERT INTO public."Author" (author_id, name) VALUES (567, 'Tom Clancy');
INSERT INTO public."Author" (author_id, name) VALUES (568, 'Steven Gould');
INSERT INTO public."Author" (author_id, name) VALUES (558, 'Brett Helquist');
INSERT INTO public."Author" (author_id, name) VALUES (582, 'Andy Weir');
INSERT INTO public."Author" (author_id, name) VALUES (590, 'Ernest Cline');
INSERT INTO public."Author" (author_id, name) VALUES (406, 'Garth Nix');
INSERT INTO public."Author" (author_id, name) VALUES (624, 'Lee Child');
INSERT INTO public."Author" (author_id, name) VALUES (592, 'Paolo Bacigalupi');
INSERT INTO public."Author" (author_id, name) VALUES (599, 'Joseph Fink');
INSERT INTO public."Author" (author_id, name) VALUES (600, 'Jeffrey Cranor');
INSERT INTO public."Author" (author_id, name) VALUES (601, 'Daniel C. Dennett');
INSERT INTO public."Author" (author_id, name) VALUES (602, 'Leo Frankowski');
INSERT INTO public."Author" (author_id, name) VALUES (607, 'Lev Grossman');
INSERT INTO public."Author" (author_id, name) VALUES (603, 'Michael Scott');
INSERT INTO public."Author" (author_id, name) VALUES (421, 'Orson Scott Card');
INSERT INTO public."Author" (author_id, name) VALUES (650, 'Ray Bradbury');
INSERT INTO public."Author" (author_id, name) VALUES (651, 'John Smith');
INSERT INTO public."Author" (author_id, name) VALUES (524, 'Peter David');
INSERT INTO public."Author" (author_id, name) VALUES (523, 'Robin Furth');
INSERT INTO public."Author" (author_id, name) VALUES (655, 'Jae Lee');
INSERT INTO public."Author" (author_id, name) VALUES (843, 'Tamas Gaspar');
INSERT INTO public."Author" (author_id, name) VALUES (470, 'Antoine Dodé');
INSERT INTO public."Author" (author_id, name) VALUES (863, 'Laurie Goulding');
INSERT INTO public."Author" (author_id, name) VALUES (869, 'M. Grant Kellermeyer');
INSERT INTO public."Author" (author_id, name) VALUES (526, 'Michael Lark');
INSERT INTO public."Author" (author_id, name) VALUES (921, 'Luke Ross');
INSERT INTO public."Author" (author_id, name) VALUES (922, 'Robin Hobb');
INSERT INTO public."Author" (author_id, name) VALUES (923, 'Paul Boehmer');
INSERT INTO public."Author" (author_id, name) VALUES (928, 'Michael R. Collings');
INSERT INTO public."Author" (author_id, name) VALUES (960, 'Diane Capri');
INSERT INTO public."Author" (author_id, name) VALUES (525, 'Richard Isanove');
INSERT INTO public."Author" (author_id, name) VALUES (986, 'Joshua Toulmin');
INSERT INTO public."Author" (author_id, name) VALUES (994, 'Paul Heitsch');
INSERT INTO public."Author" (author_id, name) VALUES (1002, 'Joshua McHenry Miller');
INSERT INTO public."Author" (author_id, name) VALUES (1005, 'B. V. Larson');
INSERT INTO public."Author" (author_id, name) VALUES (1013, 'Mark Boyett');
INSERT INTO public."Author" (author_id, name) VALUES (1017, 'Jay Allan');
INSERT INTO public."Author" (author_id, name) VALUES (1020, 'Robert Galbraith');
INSERT INTO public."Author" (author_id, name) VALUES (1036, 'Sean Williams');
INSERT INTO public."Author" (author_id, name) VALUES (1043, 'Brian Jacques');


--
-- TOC entry 3079 (class 2606 OID 19403)
-- Name: Author Author_pkey; Type: CONSTRAINT; Schema: public; Owner: s.n.azim
--

ALTER TABLE ONLY public."Author"
    ADD CONSTRAINT "Author_pkey" PRIMARY KEY (author_id);


--
-- TOC entry 3081 (class 2606 OID 19425)
-- Name: Author unique_author_name; Type: CONSTRAINT; Schema: public; Owner: s.n.azim
--

ALTER TABLE ONLY public."Author"
    ADD CONSTRAINT unique_author_name UNIQUE (name);


--
-- TOC entry 3211 (class 0 OID 0)
-- Dependencies: 198
-- Name: TABLE "Author"; Type: ACL; Schema: public; Owner: s.n.azim
--

GRANT ALL ON TABLE public."Author" TO ece651_ml;
GRANT ALL ON TABLE public."Author" TO ece651_web;
GRANT ALL ON TABLE public."Author" TO ece651_scraper;


-- Completed on 2019-03-03 10:24:46 EST

--
-- PostgreSQL database dump complete
--

