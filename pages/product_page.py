from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text

        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Adding message is not presented"
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text

        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Basket total is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert product_price in message, "No product price in the message"
