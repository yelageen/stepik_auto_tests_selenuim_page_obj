from .base_page import BasePage
from .locators  import BasketPageLocators

class BasketPage(BasePage): 
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY)

    def should_not_be_basket_title(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), 'The "Basket Items" header should not appear but it does'
