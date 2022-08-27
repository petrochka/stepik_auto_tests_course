from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))
button = browser.find_element(By.CLASS_NAME, value='btn')
browser.execute_script("window.scrollBy(0, 120);")
checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
input = browser.find_element(By.ID, value='answer')
input.send_keys(y)

button.click()
time.sleep(5)
browser.quit()
