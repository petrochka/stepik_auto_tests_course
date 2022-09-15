import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(link)
    needed_link = browser.find_element(By.LINK_TEXT, value=str(math.ceil(math.pow(math.pi, math.e)*10000)))
    needed_link.click()
    name = browser.find_element(By.TAG_NAME, value='input')
    name.send_keys("Ivan")
    lastname = browser.find_element(By.NAME, value='last_name')
    lastname.send_keys("Petrov")
    city = browser.find_element(By.CLASS_NAME, value='city')
    city.send_keys("Smolensk")
    country = browser.find_element(By.ID,value='country')
    country.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
