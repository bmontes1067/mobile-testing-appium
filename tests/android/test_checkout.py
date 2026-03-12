"""Tests del flujo de checkout completo — Android."""

import pytest
from pages.android.login_page import LoginPage
from pages.android.catalog_page import CatalogPage
from pages.android.cart_page import CartPage
from pages.android.checkout_page import CheckoutPage

pytestmark = pytest.mark.platform("android")


@pytest.fixture(autouse=True)
def setup(driver):
    """Login + añadir producto + ir al carrito antes de cada test."""
    LoginPage(driver).login("standard_user", "secret_sauce")
    catalog = CatalogPage(driver)
    catalog.add_first_item_to_cart()
    catalog.tap_cart()


class TestCheckoutAndroid:

    def test_cart_has_item(self, driver):
        """El carrito tiene exactamente 1 producto."""
        cart = CartPage(driver)
        assert cart.is_loaded()
        assert cart.get_item_count() == 1

    def test_remove_item_from_cart(self, driver):
        """Eliminar el producto deja el carrito vacío."""
        cart = CartPage(driver)
        cart.remove_first_item()
        assert cart.is_empty()

    def test_checkout_complete_flow(self, driver):
        """Flujo completo: carrito → formulario → order complete."""
        cart = CartPage(driver)
        cart.tap_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Belén", "Montes", "41001")
        checkout.tap_continue()
        checkout.tap_finish()

        assert checkout.is_order_complete(), "La pantalla de confirmación no aparece"

    def test_checkout_empty_form(self, driver):
        """Submit formulario vacío → error de campos requeridos."""
        cart = CartPage(driver)
        cart.tap_checkout()

        checkout = CheckoutPage(driver)
        checkout.tap_continue()

        assert checkout.is_visible(
            (pytest.importorskip("appium.webdriver.common.appiumby").AppiumBy.XPATH,
             '//*[contains(@text, "required")]')
        )
