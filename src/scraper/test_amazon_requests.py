#!/usr/bin/env python3
import unittest
import requests
import sys
import pprint
from bs4 import BeautifulSoup

import get_book_information as getInfo

class TestAmazonRequests(unittest.TestCase):
    def setUp(self):
        if sys.version_info[0] < 3:
            raise Exception("Must be using Python 3")
        self.pp = pprint.PrettyPrinter(indent=4)

    @classmethod
    def tearDownClass(cls):
        # print('Calling TearDown')
        getInfo.close()
    
    def test_simple_search(self):
        r = getInfo.grab_url_request(getInfo.AMAZON_SEARCH_URL, return_soup=False)

        # print(r.status_code)
        # print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(len(r.text) > 50000)
    def test_get_homepage(self):
        r = getInfo.grab_url_request('https://www.amazon.ca', return_soup=False)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(len(r.text) > 50000)


    def test_1984_book(self):
        url = 'https://www.amazon.ca/Nineteen-Eighty-Four-George-Orwell/dp/0141036141'

        book_info = getInfo.fetch_new_book_info(1,url)
        self.assertIsNotNone(book_info)
        self.assertEqual(book_info['title'], 'Nineteen Eighty Four')
        # self.pp.pprint(book_info)


    def test_search_Macbeth(self):
        book_url = getInfo.search_amazon_for_book(1,'Macbeth','William Shakespeare')
        # getInfo.close()
        self.assertIsNotNone(book_url)
        # self.pp.pprint(book_url)

                

if __name__ == '__main__':
    unittest.main()
