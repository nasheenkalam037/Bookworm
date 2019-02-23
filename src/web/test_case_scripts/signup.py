from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Chrome('/src/web/driver/chromedriver')
driver.implicitly_wait(500)
driver.get("http://127.0.0.1:3000/account/signup")


elem = driver.find_element_by_id("fullname")
elem.send_keys("Test User01")

elem = driver.find_element_by_id("email")
elem.send_keys("testuser@gmail.com")

elem = driver.find_element_by_id("password")
elem.send_keys("usertest01")

elem = driver.find_element_by_id("confirmation_password")
elem.send_keys("usertest01")

signup = driver.find_element_by_id("signup")
signup.click()


if (driver.find_element_by_xpath ("//*[contains(text(), 'Test User01')]")):
    print ("Test Passed")
else:
    print ("Test Failed")

driver.implicitly_wait(200)
driver.quit()