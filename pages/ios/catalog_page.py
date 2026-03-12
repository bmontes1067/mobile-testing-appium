"""CatalogPage iOS."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.ios.base_page import BasePage


class CatalogPage(BasePage):

    CATALOG_HEADER      = (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    ADD_TO_CART_BUTTONS = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")
    CART_BUTTON         = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    SORT_BUTTON         = (AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button")
    PRODUCT_NAMES       = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="test-Item title"]')

    SORT_AZ   = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Name (A to Z)"]')
    SORT_ZA   = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Name (Z to A)"]')
    SORT_LOHI = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Price (low to high)"]')

    def is_loaded(self) -> bool:
        return self.is_visible(self.CATALOG_HEADER)

    def get_product_names(self) -> list[str]:
        els = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in els]

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTONS)

    def tap_cart(self):
        self.click(self.CART_BUTTON)

    def sort_by(self, option: str):
        self.click(self.SORT_BUTTON)
        mapping = {"az": self.SORT_AZ, "za": self.SORT_ZA, "lohi": self.SORT_LOHI}
        self.click(mapping[option])
