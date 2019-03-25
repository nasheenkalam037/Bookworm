from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import unittest
import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from config import config

driver = None

remove_reviews_sql = 'DELETE FROM "Reviews" where user_id = %s'
def remove_user_reviews(user_id):
    try:
        params = config()
        tcp = ThreadedConnectionPool(1, 10, **params)
        conn = tcp.getconn()
        cur = conn.cursor()
        cur.execute(remove_reviews_sql, (user_id,))
        conn.commit()
    except Exception as err:
        pass


def review(self):
    global driver
    elem = driver.find_element_by_xpath("//a[contains (@href,'/account/signin')]")
    elem.click()

    remove_user_reviews(3)

    try:
        elem = driver.find_element_by_id("email")
        elem.send_keys("automation_test@gmail.com")

        elem = driver.find_element_by_id("password")
        elem.send_keys("password")

        login = driver.find_element_by_id("login")
        login.click()

    except:
        self.fail('Test Failed: Login to review failed')

    try:
        driver.get("http://127.0.0.1:3000/book/372/The%20Horus%20Heresy:%20Master%20of%20Mankind")

        elem = driver.find_element_by_xpath("//select[@name='rating']/option[text()='3']")
        elem.click()

        elem1 = driver.find_element_by_class_name('review-comment')
        elem1.clear()
        elem1.send_keys('This is a test review by automation user')

        elem2 = driver.find_element_by_class_name('review-btn')
        elem2.click()

        # review verification
        elem = driver.find_element_by_class_name('user-review-text')
        if 'This is a test review by automation user' in elem.text:
            pass
        else:
            self.fail('Test Failed: Review load error')


    except:
        self.fail('Test Failed: Review Add failed')


class BookDetailsTest(unittest.TestCase):

    def setUp(self):
        global driver
        #driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
        if not driver:
            driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        # print('Calling TearDown')
        if driver:
            driver.quit()

    def test_bookdetails(self):
        global driver

        driver.get("http://127.0.0.1:3000/book/372/The%20Horus%20Heresy:%20Master%20of%20Mankind")

        # Case 1 : Verify Routing using matching ISBN of Book
        elem = driver.find_element_by_class_name('product-detail')
        x = '978-1784967116'
        if x in elem.text:
            pass
        else:
            self.fail('Test Failed: Book detail mismatch')

        # Case 2 : Verify author information is loaded and correct
        elem = driver.find_element_by_xpath("//*[contains (@href,'/author/1509/Aaron Dembski-Bowden')]")
        if 'Aaron Dembski-Bowden' in elem.text:
            pass
        else:
            self.fail('Test Failed: Author mismatch')

        # Case 3: Synopsis loaded and correct
        synopsis='While Horus’ rebellion burns across the galaxy, a very different kind of war rages beneath the Imperial Palace.'
        elem=driver.find_element_by_xpath("//p[contains (@class,'font-normal')]")
        if synopsis in elem.text:
            pass
        else:
            self.fail('Test Failed: Synopsis mismatch')

        # Case 4: Review block verification
        review_text='Customer Reviews'
        elem = driver.find_element_by_xpath("//h4[contains (@class,'no-bottom-pm')]")
        if review_text in elem.text:
            pass
        else:
            self.fail('Test Failed: Review block loading error')


        # Case 5 : Thumbnail verification
        #cover_image = '/images/book_covers/372.jpeg'
        elem = driver.find_element_by_xpath("//img[contains(@src,'372.jpeg')]")
        if elem.size != 0:
            pass
        else:
            self.fail('Test Failed: Cover not found')

        # Case 6: sign in and review
        elem = driver.find_element_by_class_name('submit-review')
        sign_in_review='Please login to write a review for this book'

        if sign_in_review in elem.text:
            pass

        else:
            self.fail('Test Failed: Review log in link load error')

        review(self)



if __name__ == '__main__':
    unittest.main()

