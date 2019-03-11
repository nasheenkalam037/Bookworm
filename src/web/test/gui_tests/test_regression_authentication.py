from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import unittest

class RegressionTestAuthenticationSystem(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
        self.driver = webdriver.Chrome()

    def test_regressignin(self):
        # self.driver.implicitly_wait(500)
        self.driver.get("http://127.0.0.1:3000/")


        #launch application

        elem = self.driver.find_element_by_xpath("//*[contains(text(), 'Sign up')]")
        elem.click()

        #case 1 : signing up without any input
        self.signup()
        self.fieldvalidation()

        #case 2: signing up with only name

        elem=self.driver.find_element_by_id("fullname")
        elem.send_keys("Test User")
        self.signup()
        self.fieldvalidation()

        # case 3: signing up with only name and email
        elem = self.driver.find_element_by_id("email")
        elem.send_keys("tuser@gmail.com")
        self.signup()
        self.fieldvalidation()

        # case 3: signing up with only name and email and password
        elem = self.driver.find_element_by_id("password")
        elem.send_keys("abcd123")
        self.signup()
        self.fieldvalidation()

        # case 4: signing up with password mismatch
        elem = self.driver.find_element_by_id("confirmation_password")
        elem.send_keys("abcd456")

        self.signup()
        self.invalid_input()

        # case 5: duplicate email sign up
        elem = self.driver.find_element_by_id("fullname")
        elem.send_keys("Test User06")

        elem = self.driver.find_element_by_id("email")
        elem.send_keys("testuser6@gmail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("usertest04")

        elem = self.driver.find_element_by_id("confirmation_password")
        elem.send_keys("usertest04")
        self.signup()
        self.invalid_input()

        # case 6: regression user sign up

        elem = self.driver.find_element_by_id("fullname")
        elem.send_keys("Regression Test")

        elem = self.driver.find_element_by_id("email")
        elem.send_keys("regression@mail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("password")

        elem = self.driver.find_element_by_id("confirmation_password")
        elem.send_keys("password")

        self.signup()
        self.user_verification()

        # new tab and signup confirmation

        self.actions = ActionChains(self.driver)
        about = self.driver.find_element_by_link_text('TheBookworm')
        self.actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.user_verification()

        # sign out

        self.signout()

        # signin test start

        self.signin()

        # case 1: sign in with wrong password
        elem = self.driver.find_element_by_id("email")
        elem.send_keys("regression@mail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("password1")
        self.signin_button()
        self.signin_validation()

        # case 2: sign in with spaced password

        elem = self.driver.find_element_by_id("email")
        elem.send_keys("regression@mail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys(" password")
        self.signin_button()
        self.signin_validation()

        # case 3: sign in with spaced email
        elem = self.driver.find_element_by_id("email")
        elem.send_keys("regression@mail.com ")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("password")
        self.signin_button()
        self.signin_validation()

        # case 4: sign in success
        elem = self.driver.find_element_by_id("email")
        elem.send_keys("regression@mail.com")

        elem = self.driver.find_element_by_id("password")
        elem.send_keys("password")
        self.signin_button()
        self.signin_validation()


        self.tearDown()




    def signup(self):
        elem = self.driver.find_element_by_id("signup")
        elem.click()

    def signout(self):
        try:
            elem = self.driver.find_element_by_xpath("//*[contains(text(), 'Sign out')]")
            elem.click()
            #print('Test Passed: Sign out completed')
            self.signout_confirmation()
        except:
            self.fail('Test Failed: Sign out not possible')
            pass


    def signin(self):
        try:
            elem = self.driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]")
            elem.click()
            #print('Test Passed: Sign in button found')
        except:
            self.fail('Test Failed: Sign in link not found')
            pass

    def signin_button(self):
        elem = self.driver.find_element_by_id("login")
        elem.click()




    def fieldvalidation(self):
        x ='Please fill in'
        message = self.driver.find_element_by_id("email").get_attribute("validationMessage")
        message1 = self.driver.find_element_by_id("fullname").get_attribute("validationMessage")
        message2 = self.driver.find_element_by_id("password").get_attribute("validationMessage")
        message3 = self.driver.find_element_by_id("confirmation_password").get_attribute("validationMessage")

        if x in message or x in message1 or x in message2 or x in message3:
            pass
            #print("Test Passed: Empty field exists")

        else:
           self.fail()


    def invalid_input(self):
            elem = None
            try:
                elem = self.driver.find_element_by_class_name('error')
            except:
                pass

            if elem:
                if 'do not match' in elem.text:
                    pass
                    #print("Test Passed: Invalid Input")

                elif 'Duplicate Email found in table' in elem.text:
                    pass
                    #print("Test Passed: User Already Exists")
                else:
                    self.fail("Test Failed: Unexpected error")

                    #print('Unexpected error')


    def user_verification(self):
        elem_error = None
        elem_welcome = None

        try:
            elem_error = self.driver.find_element_by_class_name('error')
        except:
            pass

        try:
            elem_welcome = self.driver.find_element_by_class_name('loginbox')
        except:
            pass

        if elem_error:
            if 'did you forget' in elem_error.text:
                pass
                #print("Test Passed: Error - Credential mismatch")

        elif elem_welcome:
            page = self.driver.current_url
            if page == 'http://127.0.0.1:3000/':
                pass
                #print('Test Passed: Dashboard Loaded')
                if 'Regression Test' in elem_welcome.text:
                    pass
                    #print("Test Passed: User sign up completed - Matched")
                else:
                    # self.assertRaises('Test Failed: Wrong Username Displayed')
                    self.fail('Test Failed: Wrong Username Displayed')

                    #print('Test Failed: Wrong Username Displayed')

            else:
                self.fail("Test Failed: Dashboard not loaded")


                #self.fail("Test Failed: User creation failed: Already exists")

                # print("Test Failed: Dashboard not loaded")
                # print('Test Failed: User creation failed: Already exists')


    def signout_confirmation(self):
        elem_welcome= None
        try:
            elem_welcome = self.driver.find_element_by_class_name('loginbox')
        except:
            pass

        page = self.driver.current_url
        if page == 'http://127.0.0.1:3000/':
            pass
            #print('Test Passed: New tab Loaded')
            if 'Anonymous' in elem_welcome.text:
                pass
                #print("Test Passed: Logout complete - Anonymous found")

            else:
                self.fail('Test Failed: Logout Failed')
                #print('Test Failed: Logout Failed')

        else:
            self.fail("Test Failed: Dashboard not loaded")
            #print("Test Failed: Dashboard not loaded")


    def signin_validation(self):

        elem_error = None
        elem_welcome = None

        try:
            elem_error = self.driver.find_element_by_class_name('error')
        except:
            pass

        try:
            elem_welcome = self.driver.find_element_by_class_name('loginbox')
        except:
            pass

        if elem_error:
            if 'An error occurred when trying to setup an account' in elem_error.text:
                pass
                #print("Test Passed: Error - Credential mismatch")

        elif elem_welcome:
            page = self.driver.current_url
            if page == 'http://127.0.0.1:3000/':
                pass
                #print('Test Passed: Dashboard Loaded')
                if 'Regression Test' in elem_welcome.text:
                    pass
                    #print("Test Passed: Sign in completed: user matched")
                else:
                    self.fail("Test Failed: Wrong Username Displayed")
                    #print('Test Failed: Wrong Username Displayed')

            else:
                pass
                #print('Test Passed: Error - Credential mismatch')

        else:
            self.fail("Test Failed: Unexpected Error")
            #print("unexpected error")