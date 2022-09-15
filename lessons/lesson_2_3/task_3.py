import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12 * math.sin(value))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)
button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()
browser.switch_to.window(browser.window_handles[1])

element = browser.find_element(By.ID, 'input_value').text
answer = calc(int(element))
answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(answer)
button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()
time.sleep(5)
browser.quit()
