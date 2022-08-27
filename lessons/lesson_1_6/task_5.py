from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, value='//div[1]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, value='div.first_block > div.form-group.second_class > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value='third')
    input3.send_keys("348@mail.ru")
    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, value='btn')
    button.click()
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
