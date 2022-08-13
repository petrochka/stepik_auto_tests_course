import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage


@pytest.fixture()
def product_page_link():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_page_link):
    page = ProductPage(browser, product_page_link)
    page.open()  # открываем страницу
    page.add_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    assert page.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "add to basket message is presented"


def test_guest_cant_see_success_message(browser, product_page_link):
    page = ProductPage(browser, product_page_link)
    page.open()  # открываем страницу
    assert page.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "add to basket message is presented"


def test_message_disappeared_after_adding_product_to_basket(browser, product_page_link):
    page = ProductPage(browser, product_page_link)
    page.open()  # открываем страницу
    page.add_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    assert page.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "message of adding is not disappeared"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
