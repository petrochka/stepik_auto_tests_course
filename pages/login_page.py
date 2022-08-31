from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration form is not presented"

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert "login" in self.browser.current_url, "Login not in current url"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_input.send_keys(password)
        password_repeat_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        password_repeat_input.send_keys(password)
