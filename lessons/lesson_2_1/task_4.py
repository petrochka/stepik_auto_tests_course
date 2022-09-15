import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
chest = browser.find_element(By.ID, value="treasure")
number = chest.get_attribute("valuex")
answer = calc(number)
answer_field = browser.find_element(By.ID, value='answer')
answer_field.send_keys(answer)
checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
submit = browser.find_element(By.CLASS_NAME, value='btn')
submit.click()

time.sleep(2)
browser.quit()
