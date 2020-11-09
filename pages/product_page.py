from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def name_is_correct(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        bask_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert prod_name == bask_name, "Uncorrect product"

    def price_is_correct(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        bask_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert prod_price == bask_price, "Uncorrect price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_second_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
