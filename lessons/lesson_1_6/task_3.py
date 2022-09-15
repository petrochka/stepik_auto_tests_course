import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, value='input')
    for element in elements:
        element.send_keys("None")
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
