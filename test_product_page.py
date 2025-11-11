import pytest
from pytest_playwright.pytest_playwright import page

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# 1. Тест: Сообщения НЕ должно быть после добавления товара
# ---------------------
@pytest.mark.xfail(reason="Сообщение появляется — это известный баг по заданию")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    # ✅ assert: проверяем, что сообщение отсутствует
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


# ---------------------
# 2. Тест: Сообщения НЕ должно быть, если просто открыть страницу
# ---------------------
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    # ✅ assert
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented on product page, but should not be"


# ---------------------
# 3. Тест: Сообщение должно исчезать через пару секунд
# ---------------------
@pytest.mark.xfail(reason="Сообщение НЕ исчезает — баг по заданию")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    # ✅ assert
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message did not disappear"

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()