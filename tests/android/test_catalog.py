"""Catalog tests — Android."""

import pytest
from pages.android.login_page import LoginPage
from pages.android.catalog_page import CatalogPage

pytestmark = pytest.mark.platform("android")


@pytest.fixture(autouse=True)
def login(driver):
    """Auto-login before each catalog test."""
    LoginPage(driver).login("standard_user", "secret_sauce")


class TestCatalogAndroid:

    def test_catalog_loads_after_login(self, driver):
        """Catalog screen is displayed after login."""
        assert CatalogPage(driver).is_loaded()

    def test_catalog_shows_products(self, driver):
        """Catalog shows at least one product."""
        names = CatalogPage(driver).get_product_names()
        assert len(names) > 0, "No products found in the catalog"

    def test_sort_az(self, driver):
        """Sort A→Z returns products in alphabetical order."""
        catalog = CatalogPage(driver)
        catalog.sort_by("az")
        names = catalog.get_product_names()
        assert names == sorted(names), f"Products not in A→Z order: {names}"

    def test_sort_za(self, driver):
        """Sort Z→A returns products in reverse alphabetical order."""
        catalog = CatalogPage(driver)
        catalog.sort_by("za")
        names = catalog.get_product_names()
        assert names == sorted(names, reverse=True), "Products not in Z→A order"

    def test_add_item_to_cart(self, driver):
        """Adding a product updates the cart icon."""
        catalog = CatalogPage(driver)
        catalog.add_first_item_to_cart()
        assert catalog.is_visible(CatalogPage.CART_BUTTON)

    def test_navigate_to_cart(self, driver):
        """Tapping the cart navigates to the cart screen."""
        from pages.android.cart_page import CartPage
        catalog = CatalogPage(driver)
        catalog.tap_cart()
        assert CartPage(driver).is_loaded(), "Did not navigate to cart"
