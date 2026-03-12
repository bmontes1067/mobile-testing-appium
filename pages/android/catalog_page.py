"""CatalogPage Android — main products screen."""

from appium.webdriver.common.appiumby import AppiumBy
from pages.android.base_page import BasePage


class CatalogPage(BasePage):

    # ─── Locators ─────────────────────────────────────────────────────────────
    CATALOG_HEADER      = (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    PRODUCT_NAMES       = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Item title"]')
    SORT_BUTTON         = (AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button")
    CART_BUTTON         = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    ADD_TO_CART_BUTTONS = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")
    MENU_BUTTON         = (AppiumBy.ACCESSIBILITY_ID, "test-Menu")

    SORT_AZ   = (AppiumBy.XPATH, '//*[@text="Name (A to Z)"]')
    SORT_ZA   = (AppiumBy.XPATH, '//*[@text="Name (Z to A)"]')
    SORT_LOHI = (AppiumBy.XPATH, '//*[@text="Price (low to high)"]')
    SORT_HIOP = (AppiumBy.XPATH, '//*[@text="Price (high to low)"]')

    # ─── Actions ──────────────────────────────────────────────────────────────
    def is_loaded(self) -> bool:
        return self.is_visible(self.CATALOG_HEADER)

    def get_product_names(self) -> list[str]:
        els = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in els]

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTONS)

    def tap_cart(self):
        self.click(self.CART_BUTTON)

    def tap_sort(self):
        self.click(self.SORT_BUTTON)

    def sort_by(self, option: str):
        """
        Opens the sort modal and selects the given option.
        option: "az" | "za" | "lohi" | "hilow"
        """
        self.tap_sort()
        mapping = {
            "az":    self.SORT_AZ,
            "za":    self.SORT_ZA,
            "lohi":  self.SORT_LOHI,
            "hilow": self.SORT_HIOP,
        }
        locator = mapping.get(option)
        if not locator:
            raise ValueError(f"Invalid sort option: {option}")
        self.click(locator)

    def open_menu(self):
        self.click(self.MENU_BUTTON)
