from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, value="peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, value="robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
time.sleep(10)
browser.quit()