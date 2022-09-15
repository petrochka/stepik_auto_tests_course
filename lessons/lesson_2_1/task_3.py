import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
element = browser.find_element(By.ID, value='input_value').text
answer = calc(element)

answer_field = browser.find_element(By.ID, value='answer')
answer_field.send_keys(answer)

checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
submit = browser.find_element(By.CLASS_NAME, value='btn')
submit.click()
time.sleep(1)
browser.quit()
