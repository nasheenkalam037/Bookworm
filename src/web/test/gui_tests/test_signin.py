from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import unittest


class TestSignInUpSystem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signin(self):
        self.driver.get("http://127.0.0.1:3000/")

        elem = self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/a[1]")
        elem.click()

        #self.driver.implicitly_wait(100)

        elem = self.driver.find_element_by_id("email")
        elem.send_keys("automation_test23@gmail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("password")

        login = self.driver.find_element_by_id("login")
        login.click()

        if len(self.driver.find_elements_by_class_name('error')) > 0:
            elem = self.driver.find_element_by_id("email")
            elem.send_keys("automation_test@gmail.com")

            elem = self.driver.find_element_by_id("password")
            elem.send_keys("password")

            login = self.driver.find_element_by_id("login")
            login.click()

            elem = None
            try:
                elem = self.driver.find_element_by_id('user_welcome')
            except:
                pass

            if elem:
                if 'Hello automation_test@gmail.com' in elem.text:
                    #self.driver.implicitly_wait(200)
                    # print("Test Passed : signin completed")
                    pass
                else:
                    self.fail("Test Failed: User not found")
            else:
                self.fail("Test Failed: Container 'id=user_welcome' Not Found")

        # elif len(self.driver.find_elements_by_xpath("//*[contains(text(), 'An error occurred when trying to setup an account')]")) >0:
        #      print ("Test Failed: Username and Password combination mismatch")

        else:
            self.fail("Test Failed: Login should have failed!")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()