#!/usr/bin/env python3
import unittest
import requests
import sys
from bs4 import BeautifulSoup

import scrape_books

class TestAmazonRequests(unittest.TestCase):
    def setUp(self):
        if sys.version_info[0] < 3:
            raise Exception("Must be using Python 3")
    def test_simple_search(self):
        r = scrape_books.grab_url_request(scrape_books.AMAZON_SEARCH_URL, return_soup=False)

        # print(r.status_code)
        # print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(len(r.text) > 50000)
    def test_get_homepage(self):
        r = scrape_books.grab_url_request('https://www.amazon.ca', return_soup=False)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(len(r.text) > 50000)
        

if __name__ == '__main__':
    unittest.main()