# test_product_page.py
import pytest
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()  # <-- получаем цену со страницы товара

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_message_with_product_name(product_name)
    page.should_be_message_with_basket_price(product_price)