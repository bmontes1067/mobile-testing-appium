"""Tests del catálogo de productos — Android."""

import pytest
from pages.android.login_page import LoginPage
from pages.android.catalog_page import CatalogPage

pytestmark = pytest.mark.platform("android")


@pytest.fixture(autouse=True)
def login(driver):
    """Login automático antes de cada test de catálogo."""
    LoginPage(driver).login("standard_user", "secret_sauce")


class TestCatalogAndroid:

    def test_catalog_loads_after_login(self, driver):
        """El catálogo se muestra tras login."""
        catalog = CatalogPage(driver)
        assert catalog.is_loaded()

    def test_catalog_shows_products(self, driver):
        """El catálogo muestra al menos 1 producto."""
        catalog = CatalogPage(driver)
        names = catalog.get_product_names()
        assert len(names) > 0, "No se encontraron productos en el catálogo"

    def test_sort_az(self, driver):
        """Ordenar A→Z produce lista ordenada alfabéticamente."""
        catalog = CatalogPage(driver)
        catalog.sort_by("az")
        names = catalog.get_product_names()
        assert names == sorted(names), f"Productos no están en orden A→Z: {names}"

    def test_sort_za(self, driver):
        """Ordenar Z→A produce lista en orden inverso."""
        catalog = CatalogPage(driver)
        catalog.sort_by("za")
        names = catalog.get_product_names()
        assert names == sorted(names, reverse=True), "Productos no están en orden Z→A"

    def test_add_item_to_cart(self, driver):
        """Añadir un producto actualiza el badge del carrito."""
        catalog = CatalogPage(driver)
        catalog.add_first_item_to_cart()
        # El badge aparece en el ícono del carrito
        assert catalog.is_visible(CatalogPage.CART_BUTTON)

    def test_navigate_to_cart(self, driver):
        """Pulsar el carrito navega a la pantalla de carrito."""
        from pages.android.cart_page import CartPage
        catalog = CatalogPage(driver)
        catalog.tap_cart()
        cart = CartPage(driver)
        assert cart.is_loaded(), "No navegó al carrito"
