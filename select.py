from selenium import webdriver
import time,math
link = ""
browser = webdriver.chrome()
browser.get(link)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
# ИЛИ select.select_by_visible_text("text") и select.select_by_index(index)