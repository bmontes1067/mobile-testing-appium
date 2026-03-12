"""CartPage iOS — shopping cart screen."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.ios.base_page import BasePage


class CartPage(BasePage):

    CART_TITLE      = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your Cart"]')
    CART_ITEMS      = (AppiumBy.ACCESSIBILITY_ID, "test-Item")
    REMOVE_BUTTON   = (AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")

    def is_loaded(self) -> bool:
        return self.is_visible(self.CART_TITLE)

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_first_item(self):
        self.click(self.REMOVE_BUTTON)

    def tap_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def is_empty(self) -> bool:
        return self.get_item_count() == 0
