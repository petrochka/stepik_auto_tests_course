import unittest

from selenium import webdriver
import time

try:
    link= "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//div[1]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('third')
    input3.send_keys("348@mail.ru")
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name('btn')
    button.click()
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text


    class Test1(unittest.TestCase):
        def test_2(self):
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be 'Congratulations! You have successfully registered!'")
    # def test_2(self):
    #   self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


    if __name__ == "__main__":
        unittest.main()
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
