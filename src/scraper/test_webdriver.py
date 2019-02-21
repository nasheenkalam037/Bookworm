from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("headless")  # remove this line if you want to see the browser popup
driver = webdriver.Chrome(chrome_options=options)
url = 'https://www.amazon.ca/Clariel-Lost-Abhorsen-Garth-Nix/dp/0061561576/ref'
driver.get(url)

