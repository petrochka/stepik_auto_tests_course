import unittest

import selenium
from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestPageRegistration(unittest.TestCase):
    def check_page(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        welcome_text = ""
        try:
            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(by=By.XPATH, value='//div[1]/div[1]/input')
            input1.send_keys("Ivan")
            input2 = browser.find_element(by=By.CSS_SELECTOR,
                                          value='div.first_block > div.form-group.second_class > input')
            input2.send_keys("Petrov")
            input3 = browser.find_element(by=By.CLASS_NAME, value='third')
            input3.send_keys("348@mail.ru")
            # Отправляем заполненную форму
            button = browser.find_element(by=By.CLASS_NAME, value='btn')
            button.click()
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(by=By.TAG_NAME, value="h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
        except NoSuchElementException:
            pass

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()
            return welcome_text

    def test_1(self):
        test_text = self.check_page("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", test_text,
                             "Should be 'Congratulations! You have successfully registered!'")

    def test_2(self):
        test_text = self.check_page("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", test_text,
                             "Should be 'Congratulations! You have successfully registered!'")


if __name__ == "__main__":
    unittest.main()
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта