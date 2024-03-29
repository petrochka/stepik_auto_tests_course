from selenium.webdriver.common.by import By


class BasePageLocators:
    GO_T0_BASKET = (By.CSS_SELECTOR, "span > a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    GOODS_IN_BASKET = (By.CSS_SELECTOR, ".hidden-xs")


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
