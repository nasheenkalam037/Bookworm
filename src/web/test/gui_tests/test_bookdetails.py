from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import unittest

class BookDetailsTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
        self.driver = webdriver.Chrome()

    def test_bookdetails(self):

        self.driver.get("http://127.0.0.1:3000/")

        elem= self.driver.find_element_by_xpath("//*[contains (@href,'/book/372/The Horus Heresy: Master of Mankind')]")
        elem.click()

        # Case 1 : Verify Routing using matching ISBN of Book

        elem = self.driver.find_element_by_class_name('product-detail')
        x = '978-1784967116'
        if x in elem.text:
            pass
        else:
            self.fail('Test Failed: Book detail mismatch')

        # Case 2 : Verify author information is loaded and correct

        elem = self.driver.find_element_by_xpath("//*[contains (@href,'/author/499/Aaron Dembski-Bowden')]")
        if 'Aaron Dembski-Bowden' in elem.text:
            pass
        else:
            self.fail('Test Failed: Author mismatch')

        # Case 3: Synopsis loaded and correct

        synopsis='While Horus’ rebellion burns across the galaxy, a very different kind of war rages beneath the Imperial Palace.'
        elem=self.driver.find_element_by_xpath("//p[contains (@class,'font-normal')]")
        if synopsis in elem.text:
            pass
        else:
            self.fail('Test Failed: Synopsis mismatch')

        # Case 4: Review block verification

        review_text='Customer Reviews'
        elem = self.driver.find_element_by_xpath("//h4[contains (@class,'no-bottom-pm')]")
        if review_text in elem.text:
            pass
        else:
            self.fail('Test Failed: Review block loading error')

        # Case 5: sign in and review


        elem = self.driver.find_element_by_class_name('review')
        sign_in_review='Please login to write a review for this book'

        if sign_in_review in elem.text:
            pass

        else:
            self.fail('Test Failed: Review log in link load error')

        self.review()
        self.tearDown()

    def review(self):

        elem = self.driver.find_element_by_xpath("//a[contains (@href,'/account/signin')]")
        elem.click()

        try:
            elem = self.driver.find_element_by_id("email")
            elem.send_keys("automation_test@gmail.com")

            elem = self.driver.find_element_by_id("password")
            elem.send_keys("bookworm123")

            login = self.driver.find_element_by_id("login")
            login.click()

        except:
            self.fail('Test Failed: Login to review failed')

        try:
            elem = self.driver.find_element_by_xpath("//*[contains (@href,'/book/372/The Horus Heresy: Master of Mankind')]")
            elem.click()

            elem=self.driver.find_element_by_xpath("//select[@name='rating']/option[text()='3']")
            elem.click()

            elem1 = self.driver.find_element_by_class_name('review-comment')
            elem1.clear()
            elem1.send_keys('This is a test review by automation user')

            elem2=self.driver.find_element_by_class_name('review-btn')
            elem2.click()

            # data verification adding pending as book details page is not loading


        except:
            self.fail('Test Failed: Review Add failed')

    def tearDown(self):
        self.driver.quit()






