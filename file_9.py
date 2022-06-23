from selenium import webdriver

import time
import math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

chest = browser.find_element(By.ID, value="treasure")
x = chest.get_attribute("valuex")

y = calc(x)

input = browser.find_element(By.ID, value='answer')
input.send_keys(y)

checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
submit = browser.find_element(By.CLASS_NAME, value='btn')
submit.click()

time.sleep(10)
browser.quit()

time.sleep(10)
browser.quit()