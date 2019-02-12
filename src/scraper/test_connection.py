#!/usr/bin/env python3
import psycopg2
import unittest
import sys
from config import config

class TestPostGresConnection(unittest.TestCase):
    def setUp(self):
        if sys.version_info[0] < 3:
            raise Exception("Must be using Python 3")

    def test_simply_connect(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            self.assertEqual(len(db_version), 1)
            self.assertTrue('PostgreSQL' in db_version[0])

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            raise error
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    unittest.main()
