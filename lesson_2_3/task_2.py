from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(a):
    return str(math.log(abs(12 * math.sin(a))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
button = browser.find_element(By.CLASS_NAME, value='btn')
button.click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element(By.ID, value='input_value')
x = x_element.text
y = calc(int(x))
input = browser.find_element(By.ID, value='answer')
input.send_keys(y)
button = browser.find_element(By.CLASS_NAME, value='btn')
button.click()

time.sleep(1)
browser.quit()
