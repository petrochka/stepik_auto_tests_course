from selenium import webdriver
import math
import time

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

browser.get(link)
x_element = browser.find_element(By.ID, value='input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, value='answer')
input1.send_keys(y)

checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
submit = browser.find_element(By.CLASS_NAME, value='btn')
submit.click()

time.sleep(1)
browser.quit()