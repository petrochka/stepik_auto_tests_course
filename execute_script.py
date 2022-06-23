from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, value="button")
browser.execute_script("window.scrollBy(0, 120);")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
