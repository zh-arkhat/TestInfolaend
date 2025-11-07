# pages/product_page.py
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_success_message_with_product_name(self, expected_name):
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert expected_name == actual_name, \
            f"Expected product name '{expected_name}', but got '{actual_name}'"

    def should_be_message_with_basket_price(self, expected_price):
        actual_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert expected_price == actual_price, \
            f"Expected basket price '{expected_price}', but got '{actual_price}'"
