import math
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson_number',
                         ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_correct_in_message(browser, lesson_number):
    link = f"https://stepik.org/lesson/{lesson_number}/"
    browser.implicitly_wait(5)
    browser.get(link)

    answer = str(math.log(int(time.time())))
    answer_field = browser.find_element(By.TAG_NAME, "textarea")
    answer_field.send_keys(answer)

    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints")
    assert "Correct!" in message.text, f'Need "Correct!", got "{message}"'
