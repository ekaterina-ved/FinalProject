from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_login_page()
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        register_email_field.send_keys(email)
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        register_password_field.send_keys(password)
        register_password_repeat_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        register_password_repeat_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTOM)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        Url_link = self.browser.current_url
        assert "login" in Url_link, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
