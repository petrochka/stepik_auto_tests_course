import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12 * math.sin(value))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
button = browser.find_element(By.CLASS_NAME, value='btn')
button.click()
confirm = browser.switch_to.alert
confirm.accept()
element = browser.find_element(By.ID, value='input_value').text
answer = calc(int(element))
answer_field = browser.find_element(By.ID, value='answer')
answer_field.send_keys(answer)
button = browser.find_element(By.CLASS_NAME, value='btn')
button.click()

time.sleep(1)
browser.quit()
