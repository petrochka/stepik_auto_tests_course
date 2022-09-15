import time

from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket_exists(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "Button not found"
