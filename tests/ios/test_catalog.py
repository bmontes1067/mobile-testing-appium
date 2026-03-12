"""Tests del catálogo — iOS."""

import pytest
from pages.ios.login_page import LoginPage
from pages.ios.catalog_page import CatalogPage

pytestmark = pytest.mark.platform("ios")


@pytest.fixture(autouse=True)
def login(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")


class TestCatalogIOS:

    def test_catalog_loads(self, driver):
        assert CatalogPage(driver).is_loaded()

    def test_catalog_shows_products(self, driver):
        names = CatalogPage(driver).get_product_names()
        assert len(names) > 0

    def test_sort_az(self, driver):
        catalog = CatalogPage(driver)
        catalog.sort_by("az")
        names = catalog.get_product_names()
        assert names == sorted(names)

    def test_add_to_cart_and_navigate(self, driver):
        from pages.ios.cart_page import CartPage
        catalog = CatalogPage(driver)
        catalog.add_first_item_to_cart()
        catalog.tap_cart()
        assert CartPage(driver).is_loaded()
