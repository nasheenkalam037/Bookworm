from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
#driver.implicitly_wait(500)
# READ ME: DO NOT USE driver.implicitly_wait with CHROME, see https://stackoverflow.com/questions/17462884/is-selenium-slow-or-is-my-code-wrong
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

elem = None
try:
    elem = driver.find_element_by_id('error_msg')
except:
    pass

if elem:
    if 'do not match' in elem.text:
        print ("Test Passed - Invalid Input")
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

        elem_error = None
        elem_welcome = None

        try:
            elem_error = driver.find_element_by_id('error_msg')
        except:
            pass
        
        try:
            elem_welcome = driver.find_element_by_id('error_msg')
        except:
            pass

        if elem_error:
            if 'did you forget' in elem_error.text:
                print("Test Passed: Error - User Already Exists")
        elif elem_welcome:
            if 'Test User06' in elem_welcome.text:
                print ("Test Passed: User created")
            else:
                print('Test Failed: Wrong Username Displayed')


elif 'Duplicate Email found in table' in elem.text:
    print("Test Passed - User Already Exists")

else:
    print ("Test Failed")

#driver.implicitly_wait(200)
driver.quit()