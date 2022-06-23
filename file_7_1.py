from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(x))))
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
x_element = browser.find_element(By.ID, value='input_value')
x = x_element.text
y = int(calc(x))
button = browser.find_element(By.TAG_NAME, value="button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
input = browser.find_element(By.ID, value='answer')
input.send_keys(y)
button.click()
time.sleep(2)
browser.quit()