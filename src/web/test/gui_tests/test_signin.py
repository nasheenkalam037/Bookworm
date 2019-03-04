from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import unittest

class TestSignInUpSystem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signin(self):
        self.driver.implicitly_wait(500)
        self.driver.get("http://127.0.0.1:3000/")


        elem = self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/a[1]")
        elem.click()

        self.driver.implicitly_wait(100)

        elem = self.driver.find_element_by_id("email")
        elem.send_keys("automation_test@gmail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("bookworm123")

        login=self.driver.find_element_by_id("login")
        login.click()

        self.driver.implicitly_wait(500)

        if (self.driver.find_element_by_xpath(("//*[contains(text(), 'Hello Automation User')]"))):
            print ("Test Passed")
        else:
            print ("Test Failed")

    def tearDown(self):
        self.driver.implicitly_wait(200)
        self.driver.quit()