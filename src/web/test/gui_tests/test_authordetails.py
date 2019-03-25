from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import unittest


def bookListload(self):
    # Block header check

    book = 'Books By this Author'
    elem = self.driver.find_element_by_css_selector('.heading.font-xlarge')

    if book in elem.text:
        pass
    else:
        self.fail('Test Failed: Book list block not found')

    # Book details - name, synopsis

    elem = self.driver.find_elements_by_xpath("//*[contains (@class,'book-details')]")
    book2 = 'The Horus Heresy: The First Heretic'
    synopsis = 'Chastised by the Emperor, the Word Bearers set out on their own path'
    details = ''

    for i in elem:
        details = details + i.text

    if book2 in details:
        pass
    else:
        self.fail('Test Failed: Book title load acc to author failed')

    if synopsis in details:
        pass
    else:
        self.fail('Test Failed: Synopsis load failed')

    # Book Details - Book cover image

    elem = self.driver.find_element_by_xpath("//img[contains(@src,'599.jpeg')]")
    if elem.size != 0:
        pass
    else:
        self.fail('Test Failed: Book Cover not found')


def bookDeals(self):
    elem = self.driver.find_element_by_class_name('book-deal')

    elem1 = self.driver.find_elements_by_xpath("//li[contains(@class,'font-normal')]")
    deal_details = ''

    for i in elem1:
        deal_details = deal_details + i.text

    if 'Rating' in deal_details:
        pass
    else:
        self.fail("Test Failed: Vendor information Rating load error")

    if 'Review' in deal_details:
        pass
    else:
        self.fail("Test Failed: Vendor information Reviews load error")

    # Route to vendor and get book
    link_text = 'Click here to Buy'
    elem = self.driver.find_element_by_xpath(
        "//a[contains (@href,'https://www.amazon.ca/First-Heretic-Horus-Heresy/dp/1844168859?ref=pf_vv_at_pdctrvw_dp')]")

    if link_text == elem.text:
        pass
    else:
        self.fail('Test Failed: Link Text mismatch')

    elem.click()

    # Link verification using ISBN -10 code of the book

    elem = self.driver.find_element_by_xpath("//td[contains(@class,'bucket')]")
    ISBN_10 = '1844168859'

    if ISBN_10 in elem.text:
        pass
    else:
        self.fail("Test Failed: Vendor Book details mismatch")


def tearDown(self):
    self.driver.quit()

class AuthorDetailsTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
        self.driver = webdriver.Chrome()

    def test_authordetails(self):
        self.driver.get("http://127.0.0.1:3000/author/1509/Aaron%20Dembski-Bowden")


        # Case 1 : Verify Routing using matching Title of Author
        elem= self.driver.find_element_by_class_name('no-bottom-pm')
        name='Aaron Dembski-Bowden'

        if name in elem.text:
            pass
        else:
            self.fail('Test Failed: Author mismatch')

        # Case 2 : Author Picture check

        elem = self.driver.find_element_by_xpath("//img[contains(@src,'1509.jpeg')]")
        if elem.size != 0:
            pass
        else:
            self.fail('Test Failed: Author Cover Image not found')

        # Case 3 : Author book list details check

        bookListload(self)

        # Case 4 : Book deal and Get book

        bookDeals(self)

    def tearDown(self):
       if self.driver:
           self.driver.quit()










