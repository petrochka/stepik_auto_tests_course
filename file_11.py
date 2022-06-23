from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
a_element = browser.find_element(By.ID, value='num1')
a = a_element.text
b_element = browser.find_element(By.ID, value='num2')
b = b_element.text
sum = int(a) + int(b)
from selenium.webdriver.support.ui import Select

select = Select(browser.find_element(By.TAG_NAME, value="select"))
select.select_by_value(str(sum))
browser.find_element(By.CLASS_NAME, value="btn").click()
# browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("[value=]").click()
# browser.find_element_by_class_name("btn").click()
time.sleep(10)
browser.quit()
time.sleep(10)
browser.quit()
