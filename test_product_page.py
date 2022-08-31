import time

import pytest

from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.fixture
def coders_at_work_page_link():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture
def coders_at_work_promo_page_link():
    return "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.fixture
def city_and_stars_page_link():
    return "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser, coders_at_work_page_link):
        page = ProductPage(browser, coders_at_work_page_link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Message is presented"

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, coders_at_work_promo_page_link):
        page = ProductPage(browser, coders_at_work_promo_page_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, coders_at_work_promo_page_link):
    page = ProductPage(browser, coders_at_work_promo_page_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, coders_at_work_page_link):
    page = ProductPage(browser, coders_at_work_page_link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Add to basket message is presented"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, coders_at_work_page_link):
    page = ProductPage(browser, coders_at_work_page_link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Message of adding is not disappeared"


def test_guest_should_see_login_link_on_product_page(browser, city_and_stars_page_link):
    page = ProductPage(browser, city_and_stars_page_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, city_and_stars_page_link):
    page = ProductPage(browser, city_and_stars_page_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, city_and_stars_page_link):
    page = ProductPage(browser, city_and_stars_page_link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, city_and_stars_page_link)
    page.should_be_no_goods_in_basket()
    page.should_be_empty_basket_message()


def test_guest_cant_see_success_message(browser, coders_at_work_page_link):
    page = ProductPage(browser, coders_at_work_page_link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Add to basket message is presented"
