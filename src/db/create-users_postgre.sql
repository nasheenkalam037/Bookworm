CREATE USER ece651_scraper WITH
    PASSWORD 'wxJcTdJYUU3mMAsAa5YD'
    LOGIN
    NOSUPERUSER
    NOINHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION;

CREATE USER ece651_ml WITH
    PASSWORD 'TVL3MV0mguz0DOhLbbm2'
    LOGIN
    NOSUPERUSER
    NOINHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION;
CREATE USER ece651_web WITH
    PASSWORD 'dm2fBdodbrHPtJVvlSKF'
    LOGIN
    NOSUPERUSER
    NOINHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION;

CREATE DATABASE ece651
    WITH 
    OWNER = ece651_scraper

GRANT CONNECT ON DATABASE ece651 TO ece651_ml;
GRANT CONNECT ON DATABASE ece651 TO ece651_web;
GRANT CONNECT ON DATABASE ece651 TO ece651_scraper;
