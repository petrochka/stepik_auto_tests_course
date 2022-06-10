from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
result = int(num1) + int(num2)

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_visible_text(str(result))

option = browser.find_element_by_class_name('btn')
option.click()