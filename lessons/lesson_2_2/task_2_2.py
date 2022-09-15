import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element(By.ID, 'input_value').text
answer = str(math.log(abs(12*math.sin(int(element)))))
button = browser.find_element(By.CLASS_NAME, value='btn')
browser.execute_script("window.scrollBy(0, 120);")
checkbox = browser.find_element(By.ID, value='robotCheckbox')
checkbox.click()
radio = browser.find_element(By.ID, value='robotsRule')
radio.click()
answer_field = browser.find_element(By.ID, value='answer')
answer_field.send_keys(answer)

button.click()
time.sleep(5)
browser.quit()
