from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
keyword = "agile testing lisa crispin"
driver = webdriver.Chrome('/home/nasheen/Documents/ECE651/chromedriver')
driver.implicitly_wait(500)
driver.get("https://www.chapters.indigo.ca/en-ca/")
#assert "Indigo" in driver.title
#driver.implicitly_wait(500)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,"browsepopup-closebtn"))).click()


elem = driver.find_element_by_id("header__quick-search")
elem.send_keys(keyword)
driver.implicitly_wait(1000)

elem = driver.find_element_by_class_name("quick-search__submit")
elem.click()
driver.implicitly_wait(500)

elem = driver.find_element_by_xpath('//*[@title="Agile Testing: A Practical Guide for Testers and Agile Teams"]');
elem.click();
driver.implicitly_wait(500)


if (driver.find_element_by_xpath(("//*[contains(text(), 'December 30, 2008')]"))):
    print "Test Passed"
else:
    print "Test Failed"
driver.close()