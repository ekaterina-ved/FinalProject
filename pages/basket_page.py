from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_zero_amount(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Some product in basket"

    def should_be_text_about_empty_basket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert basket_text == "Your basket is empty. Continue shopping", \
            "No text about empty basket, but should be"
