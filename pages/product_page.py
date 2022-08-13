from pages.base_page import BasePage
from pages.locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
