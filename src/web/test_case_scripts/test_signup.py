from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
driver.implicitly_wait(500)
driver.get("http://127.0.0.1:3000/account/signup")


elem = driver.find_element_by_id("fullname")
elem.send_keys("Test User04")

elem = driver.find_element_by_id("email")
elem.send_keys("testuser4@gmail.com")

elem = driver.find_element_by_id("password")
elem.send_keys("usertest05")

elem = driver.find_element_by_id("confirmation_password")
elem.send_keys("usertest09")

signup = driver.find_element_by_id("signup")
signup.click()


if len(driver.find_elements_by_xpath ("//*[contains(., 'do not match')]"))>0:
    print ("Invalid Input")
    elem = driver.find_element_by_id("fullname")
    elem.send_keys("Test User06")

    elem = driver.find_element_by_id("email")
    elem.send_keys("testuser6@gmail.com")

    elem = driver.find_element_by_id("password")
    elem.send_keys("usertest04")

    elem = driver.find_element_by_id("confirmation_password")
    elem.send_keys("usertest04")

    signup = driver.find_element_by_id("signup")
    signup.click()

    if len(driver.find_elements_by_xpath("//*[contains(text(), 'Test User06')]")) > 0:
        print ("Test Passed: User created")

    elif len(driver.find_elements_by_xpath("//*[contains(.,'did you forget')]")) > 0:
        print("User Already Exists")

elif len(driver.find_elements_by_xpath ("//*[contains(., 'Duplicate Email found in table')]"))>0:
    print("User Already Exists")

else:
    print ("Test Failed")

#driver.implicitly_wait(200)
driver.quit()