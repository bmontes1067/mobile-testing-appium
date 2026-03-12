"""Full checkout flow tests — Android."""

import pytest
from pages.android.login_page import LoginPage
from pages.android.catalog_page import CatalogPage
from pages.android.cart_page import CartPage
from pages.android.checkout_page import CheckoutPage

pytestmark = pytest.mark.platform("android")


@pytest.fixture(autouse=True)
def setup(driver):
    """Login + add a product + go to cart before each test."""
    LoginPage(driver).login("standard_user", "secret_sauce")
    catalog = CatalogPage(driver)
    catalog.add_first_item_to_cart()
    catalog.tap_cart()


class TestCheckoutAndroid:

    def test_cart_has_item(self, driver):
        """Cart contains exactly one product."""
        cart = CartPage(driver)
        assert cart.is_loaded()
        assert cart.get_item_count() == 1

    def test_remove_item_from_cart(self, driver):
        """Removing the product leaves the cart empty."""
        cart = CartPage(driver)
        cart.remove_first_item()
        assert cart.is_empty()

    def test_checkout_complete_flow(self, driver):
        """Full flow: cart → form → order complete screen."""
        cart = CartPage(driver)
        cart.tap_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Belen", "Montes", "41001")
        checkout.tap_continue()
        checkout.tap_finish()

        assert checkout.is_order_complete(), "Order confirmation screen not shown"

    def test_checkout_empty_form(self, driver):
        """Submitting an empty form shows required field errors."""
        cart = CartPage(driver)
        cart.tap_checkout()

        checkout = CheckoutPage(driver)
        checkout.tap_continue()

        assert checkout.is_visible(checkout.ERROR_MESSAGE), "Required field error not shown"
