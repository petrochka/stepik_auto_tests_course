import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(link)
    name = browser.find_element(By.TAG_NAME, value='input')
    name.send_keys("Ivan")
    lastname = browser.find_element(By.NAME, value='last_name')
    lastname.send_keys("Petrov")
    city = browser.find_element(By.CLASS_NAME, value='city')
    city.send_keys("Smolensk")
    country = browser.find_element(By.ID, value='country')
    country.send_keys("Russia")
    button = browser.find_element(By.XPATH, value='/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
