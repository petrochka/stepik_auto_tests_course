from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, value='num1')
x = x_element.text
y_element = browser.find_element(By.ID, value='num2')
y = y_element.text
num = int(x) + int(y)
print(num)

browser.quit()
# browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("option:nth-child(2)").click()
