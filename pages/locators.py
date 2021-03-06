from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTOM = (By.CSS_SELECTOR, "[name=registration_submit]")

class ProductPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe strong")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")