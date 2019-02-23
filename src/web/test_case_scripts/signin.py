from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
# keyword = "agile testing lisa crispin"
driver = webdriver.Chrome()
# driver = webdriver.Chrome('/src/web/driver/chromedriver')
driver.implicitly_wait(500)
driver.get("http://127.0.0.1:3000/")


elem = driver.find_element_by_xpath("/html/body/header/div/div/div[2]/a[1]")
elem.click()

driver.implicitly_wait(100)

elem = driver.find_element_by_id("email")
elem.send_keys("automation_test@gmail.com")

elem = driver.find_element_by_id("password")
elem.send_keys("bookworm123")

login=driver.find_element_by_id("login")
login.click()

driver.implicitly_wait(500)

if (driver.find_element_by_xpath(("//*[contains(text(), 'Hello Automation User')]"))):
    print ("Test Passed")
else:
    print ("Test Failed")
driver.implicitly_wait(200)
driver.quit()