from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import unittest


def searchPageConfirmation(self, param):
    page = self.driver.current_url
    if param in page:
        pass
        value = self.driver.find_element_by_id("searchBox").get_attribute("value")
        if param in value:
            pass
        else:
            self.fail("Test Fail: Search parameter wrong")
    else:
        self.fail("Test fail: search page broken")



def searchResultCount(self):
    try:
        searchcount = self.driver.find_element_by_xpath("//*[contains(text(), 'books matching')]")
        pass

    except:
        self.fail("Test Failed: search result load error")



def searchResultVerification(self):
    try:
        searchresult = self.driver.find_element_by_xpath("//*[contains(text(), 'Holt McDougal Library, High School with Connections: Individual Reader 1984')]")
        pass

    except:
        self.fail("Test Failed: search result incorrect")


def nullResultVerification(self):
    try:
        searchresult = self.driver.find_element_by_xpath("//*[contains(., 'Sorry, we could not find the book you were looking for.')]")
        pass

    except:
        self.fail("Test Failed: search result incorrect")

class Searchtest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/")

    def test_search(self):
        search_box = self.driver.find_element_by_class_name("input-field")

        # case 1: test with positive case: should find result

        param='1984'
        search_box.send_keys(param,Keys.RETURN)
        searchPageConfirmation(self,param)
        searchResultCount(self)
        searchResultVerification(self)

        # case 2: test with negative case: should not find any result

        search_box = self.driver.find_element_by_class_name("input-field")
        search_box.clear()
        #param2='1984'
        param2 = 'sdfgsdfgsdfgsdfgdsfgsfgsdfgsdfg'
        search_box.send_keys(param2, Keys.RETURN)
        searchPageConfirmation(self,param2)
        searchResultCount(self)
        nullResultVerification(self)

        #tearDown(self)














