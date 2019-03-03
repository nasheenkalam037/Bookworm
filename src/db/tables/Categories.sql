--
-- PostgreSQL database dump
--

-- Dumped from database version 11.1
-- Dumped by pg_dump version 11.1

-- Started on 2019-03-03 10:26:33 EST

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
-- TOC entry 206 (class 1259 OID 19308)
-- Name: Categories; Type: TABLE; Schema: public; Owner: s.n.azim
--

CREATE TABLE public."Categories" (
    categories_id integer DEFAULT nextval('public."Categories_categories_id_sequence"'::regclass) NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public."Categories" OWNER TO "s.n.azim";

--
-- TOC entry 3204 (class 0 OID 19308)
-- Dependencies: 206
-- Data for Name: Categories; Type: TABLE DATA; Schema: public; Owner: s.n.azim
--

COPY public."Categories" (categories_id, name) FROM stdin;
250	Children's & Teens
725	Atomic & Nuclear Physics
508	Waves & Wave Mechanics
778	Genetic Engineering
245	Dictionaries & Thesauruses
242	Education & Reference
860	Assembly Language Programming
783	Dystopian
698	Short Stories & Anthologies
490	Military
534	Pure Mathematics
149	Textbooks
652	Fantasy & Magic
1581	Space Marine
455	Mystery, Thriller & Suspense
160	Movies
510	Particle Physics
460	Thrillers & Suspense
514	Nuclear Physics
517	Biographical
584	Asian
531	Russian
949	Networking & Cloud Computing
1576	Space Opera
760	Girls & Women
961	Legal
975	Historical Fiction
399	Ethics & Morality
972	History & Historical Fiction
454	Thrillers
549	Study & Teaching
759	Growing Up & Facts of Life
969	Crime
551	Encyclopedias
621	Adventure & Thrillers
921	Suspense
944	Cryptography
143	Politics & Social Sciences
843	Real-Time Data Processing
839	Graphic Design
171	Classics
354	Greek
802	Genetic
353	Ancient & Medieval Literature
4860	Ancient Civilizations
566	Tolkien's Middle Earth
248	Christian Books & Bibles
548	Reference
486	Differential Equations
146	World Literature
711	Gay & Lesbian
682	War & Military
513	Professional & Technical
4242	African
875	German
367	History & Surveys
396	Europe
251	Series
476	Science
567	Fluid Mechanics
608	Teens
766	Values
249	C. S. Lewis
244	Computer Dictionaries
145	Good & Evil
570	Dynamics
750	Relativity
574	Mechanical
501	Victorian
167	Literary
734	Humour
857	Computer Science & Information Systems
144	Philosophy
571	Fluid Dynamics
246	Slang & Idioms
489	Physics
147	Humanities
504	Romance
497	War
712	Lesbian
816	Mechanics
644	Gothic
485	Mathematics
360	Greek & Roman
563	Fantasy
359	Ancient
469	Post-Apocalyptic
150	Drama & Plays
240	Computers & Technology
253	Science Fiction
370	Ancient & Classical
561	Epic
842	Desktop Publishing
163	Humour & Entertainment
446	Occult
840	Graphics & Multimedia
929	India
966	Education
239	Programming
971	Military & Wars
164	Surrealism
395	History
933	Asia
161	Screenplays
159	Movements & Periods
895	Comedy
758	Friendship, Social Skills & School Life
247	Computer
798	Theory of Computing
708	Fiction
702	Anthologies
521	United States
695	Short Stories
458	Historical
717	Criticism & Theory
767	Family Life
855	Programming Languages
483	Applied
801	Artificial Life
946	Network Security
148	Shakespeare
806	Algorithms
442	Horror
615	Sea Adventures
515	Professional Science
481	Sciences
948	Software
477	Science & Math
800	Artificial Intelligence
4236	Mythology
153	British & Irish
532	Algebra & Trigonometry
4238	Norse
154	European
575	Engineering
619	Sea Stories
151	Literature
478	Statistics
743	Electrodynamics
797	Family Saga
4239	Egyptian
810	Canadian
241	Introductory & Beginning
426	Genre Fiction
535	Calculus
387	Greece
748	Computer Science
2352	IDW Publishing
2220	Parenting & Relationships
2613	Spies & Politics
996	Spanish & Portuguese
2206	Intermediate Readers
2179	Movements
1010	Computer Mathematics
1014	Mathematical & Statistical
2366	Gothic & Romantic
1255	Astrophysics & Space Science
747	Circuitry
2027	Nursery Rhymes
2370	Genres & Styles
1062	Mathematical Analysis
2032	Poetry
2307	Social Issues
2638	Themes & Styles
2226	Health
1801	Abuse
1803	Dysfunctional Relationships
1806	Difficult Discussions
2227	Personal Hygiene
1103	Magic & Wizards
2499	Fantasy Graphic Novels
2063	Research
1132	Modernism
2064	Rhetoric
2069	Writing, Research & Publishing Guides
1121	Cultural Heritage
2070	Words, Language & Grammar
2071	Writing Skills
1832	Algebra
1021	Australian & Oceania
1180	20th Century
2376	Manga
2073	Probability & Statistics
2153	Biographies & Memoirs
2699	Dark Humour
1205	Geography & Cultures
1206	Explore the World
2655	Hard Science Fiction
1214	Caribbean & Latin American
2114	First Contact
1079	Political
1087	Cats, Dogs & Animals
1208	Orphans & Foster Homes
1085	Satire
430	TV, Movie & Video Game Adaptations
1051	French
2218	Psychology
2597	Thriller & Suspense
2648	Technothrillers
2893	Cyberpunk
2701	Humour & Satire
2138	Modern
2136	Religion & Spirituality
2743	Mythology & Folk Tales
1027	Traditional Detectives
2857	Media Tie-In
1286	Mechanical Engineering
1305	Science for Kids
1054	Astronomy
2269	Internal Medicine
2270	Neurology
1320	Dragons
2808	Halloween
1353	Optics
1356	Electrical & Electronics
2161	Political History
1362	Optoelectronics
2163	History, 17th & 18th Century
530	Regional & Cultural
157	History & Criticism
2272	Medicine
4283	Russia
2170	Epistemology
2275	Neuroscience
1228	Small Town & Rural
1352	Creative Writing & Composition
2826	Exploration
2276	Medical Books
2176	Alternative Medicine
2274	By Topic
1118	Alternate History
2177	Pragmatism
2277	Intelligence
2162	Political Science
2922	Parodies & Satires
2279	Cognitive
2180	Logic & Language
2097	Time Travel
2800	Women's Fiction
2187	Experiments & Projects
2143	Germany
2197	Chapter Books & Readers
856	Languages & Tools
156	English Literature
2326	Short Story Collections
1058	Solar System
2146	Social Philosophy
2422	Criticism
2801	Domestic Life
4984	Keys to the Kingdom
2154	Reference & Collections
2402	Women's Adventure
2150	Philosophers
2932	Theology
2810	Activity Books
1325	Science, Nature & How It Works
1015	Mysteries & Detectives
2805	Hoodies & Sweatshirts
2806	Holidays & Celebrations
2811	Activities, Crafts & Games
2812	Clothing & Accessories
2813	Men
4284	Travel
2149	Professionals & Academics
981	Romantic
2202	Boys & Men
2306	Friendship
2289	Contemporary
1322	Zoology
2663	Heist
2678	Spine-Chilling Horror
4971	Private Investigators
2834	Space Fleet
2645	Alien Invasion
2501	Adaptations
2928	Theism
978	Erotica
1097	Discworld
1059	Cosmology
2796	DC
1020	Comics & Graphic Novels
2173	Health, Fitness & Dieting
2157	Social Sciences
2348	Graphic Novels
2926	Philosophy of Religion
988	Mystery
2856	Lawyers & Criminals
2350	Publishers
2723	Galactic Empire
474	Science Fiction & Fantasy
1323	Fairy Tales, Folk Tales & Myths
2409	Colonization
2698	Siblings
2978	Developmental Psychology
2983	Gender
2985	Jungian
2992	Organized Crime
3010	Zombies
3015	Zombies, Vampires & Werewolves
3016	Vampires
3018	Political Theory
3023	Comparative Government
3024	Leadership
3025	Politics
3038	Medical
4622	Financial
4634	Kidnapping
3155	Sexuality
3156	Sex
3158	Sex Instruction
3161	Human
3163	Alternative
3094	Serial Killers
3327	Psychological Thrillers
3486	Military Science
3487	Weapons & Warfare
3489	Strategy
3491	Superheroes
3078	Hard-Boiled
831	Ghosts
3736	Mysteries
3209	Essays
3211	Memoirs
1300	Science Studies
3973	Ages 9-12
3335	Supernatural
2155	Leaders & Notable People
5201	Animals
494	Action & Adventure
606	Children's Books
2221	Psychology & Counseling
152	Literature & Fiction
4074	Musical Genres
4075	Songwriting
4077	Rock
4078	Punk
4079	Theory, Composition & Performance
4080	Music
142	Books
3034	Men's Adventure
3087	Murder
\.


--
-- TOC entry 3079 (class 2606 OID 19411)
-- Name: Categories Categories_pkey; Type: CONSTRAINT; Schema: public; Owner: s.n.azim
--

ALTER TABLE ONLY public."Categories"
    ADD CONSTRAINT "Categories_pkey" PRIMARY KEY (categories_id);


--
-- TOC entry 3081 (class 2606 OID 19417)
-- Name: Categories unique_cat_name; Type: CONSTRAINT; Schema: public; Owner: s.n.azim
--

ALTER TABLE ONLY public."Categories"
    ADD CONSTRAINT unique_cat_name UNIQUE (name);


--
-- TOC entry 3210 (class 0 OID 0)
-- Dependencies: 206
-- Name: TABLE "Categories"; Type: ACL; Schema: public; Owner: s.n.azim
--

GRANT ALL ON TABLE public."Categories" TO ece651_ml;
GRANT ALL ON TABLE public."Categories" TO ece651_web;
GRANT ALL ON TABLE public."Categories" TO ece651_scraper;


-- Completed on 2019-03-03 10:26:33 EST

--
-- PostgreSQL database dump complete
--

