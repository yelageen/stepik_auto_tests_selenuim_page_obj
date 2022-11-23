import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', [
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear", marks=pytest.mark.xfail),
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_message_title()


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_message_title()


@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear", marks=pytest.mark.xfail),
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_message_title()
