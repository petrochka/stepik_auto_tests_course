import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
name = browser.find_element(By.NAME, value='firstname')
name.send_keys('Lina')
lastname = browser.find_element(By.NAME, value='lastname')
lastname.send_keys('Vasko')
email = browser.find_element(By.NAME, value='email')
email.send_keys('linavasko11@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '../venv/txt.txt')  # добавляем к этому пути имя файла
download = browser.find_element(By.ID, value='file')
download.send_keys(file_path)
button = browser.find_element(By.CLASS_NAME, value='btn')
button.click()

time.sleep(5)
browser.quit()
