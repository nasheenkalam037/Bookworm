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

    def test_signup(self):
        self.driver.get("http://127.0.0.1:3000/account/signup")

        elem = self.driver.find_element_by_id("fullname")
        elem.send_keys("Test User04")

        elem = self.driver.find_element_by_id("email")
        elem.send_keys("testuser4@gmail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("usertest05")

        elem = self.driver.find_element_by_id("confirmation_password")
        elem.send_keys("usertest09")

        signup = self.driver.find_element_by_id("signup")
        signup.click()

        elem = None
        try:
            elem = self.driver.find_element_by_id('error_msg')
        except:
            pass

        if elem:
            if 'do not match' in elem.text:
                elem = self.driver.find_element_by_id("fullname")
                elem.send_keys("Automation User")

                elem = self.driver.find_element_by_id("email")
                elem.send_keys("automation_test@gmail.com")

                elem = self.driver.find_element_by_id("password")
                elem.send_keys("bookworm123")

                elem = self.driver.find_element_by_id("confirmation_password")
                elem.send_keys("bookworm123")

                signup = self.driver.find_element_by_id("signup")
                signup.click()

                elem_error = None
                elem_welcome = None

                try:
                    elem_error = self.driver.find_element_by_id('error_msg')
                except:
                    pass
                
                try:
                    elem_welcome = self.driver.find_element_by_id('user_welcome')
                except:
                    pass

                if elem_error:
                    if 'did you forget' in elem_error.text:
                        print("Test Passed: Error - User Already Exists")
                elif elem_welcome:
                    if 'Automation User' in elem_welcome.text:
                        print ("Test Passed: User created")
                    else:
                        self.fail('Test Failed: Wrong Username Displayed')


        elif 'Duplicate Email found in table' in elem.text:
            print("Test Passed - User Already Exists")

        else:
            self.fail("Test Failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()