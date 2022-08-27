from selenium import webdriver
import time, math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)
button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()
browser.switch_to.window(browser.window_handles[1])

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(int(x))
input = browser.find_element(By.ID, 'answer')
input.send_keys(y)
button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()
time.sleep(5)
browser.quit()
