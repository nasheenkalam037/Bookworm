#!/usr/bin/env python3
import unittest
import sys
from selenium import webdriver

class TestPostGresConnection(unittest.TestCase):
    def setUp(self):
        if sys.version_info[0] < 3:
            raise Exception("Must be using Python 3")

    def test_webdriver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")  # remove this line if you want to see the browser popup
        driver = webdriver.Chrome(options=options)
        url = 'https://www.amazon.ca/Clariel-Lost-Abhorsen-Garth-Nix/dp/0061561576/ref'
        driver.get(url)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
