import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
element = browser.find_element(By.ID, value='input_value').text
answer = calc(element)
answer_field = browser.find_element(By.ID, value='answer')
answer_field.send_keys(answer)
button = browser.find_element(By.TAG_NAME, value="button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()

button.click()
time.sleep(2)
browser.quit()
