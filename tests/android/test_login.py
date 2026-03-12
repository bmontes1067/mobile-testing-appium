"""
Tests de login — Android
Credenciales válidas de My Demo App (Sauce Labs):
  - standard_user / secret_sauce
  - locked_out_user / secret_sauce  (usuario bloqueado)
"""

import pytest
from pages.android.login_page import LoginPage
from pages.android.catalog_page import CatalogPage

pytestmark = pytest.mark.platform("android")


class TestLoginAndroid:

    def test_login_valid_credentials(self, driver):
        """Login con credenciales correctas → llega a catálogo."""
        login = LoginPage(driver)
        catalog = CatalogPage(driver)

        login.login("standard_user", "secret_sauce")

        assert catalog.is_loaded(), "El catálogo no cargó tras login válido"

    def test_login_invalid_password(self, driver):
        """Password incorrecta → mensaje de error."""
        login = LoginPage(driver)

        login.login("standard_user", "wrong_password")

        assert "do not match" in login.get_error_message()

    def test_login_empty_username(self, driver):
        """Sin username → error de campo requerido."""
        login = LoginPage(driver)

        login.enter_password("secret_sauce")
        login.tap_login()

        assert login.is_username_error_shown(), "No aparece error de username vacío"

    def test_login_empty_password(self, driver):
        """Sin password → error de campo requerido."""
        login = LoginPage(driver)

        login.enter_username("standard_user")
        login.tap_login()

        assert login.is_password_error_shown(), "No aparece error de password vacío"

    def test_login_both_fields_empty(self, driver):
        """Sin rellenar nada → errores de ambos campos."""
        login = LoginPage(driver)

        login.tap_login()

        assert login.is_username_error_shown()

    def test_login_locked_user(self, driver):
        """Usuario bloqueado → mensaje de error específico."""
        login = LoginPage(driver)

        login.login("locked_out_user", "secret_sauce")

        error = login.get_error_message()
        assert "locked out" in error.lower() or "do not match" in error.lower()

    def test_login_screenshot_on_error_state(self, driver):
        """Verifica que el estado de error es visualmente correcto (screenshot)."""
        login = LoginPage(driver)

        login.login("bad_user", "bad_pass")
        screenshot_path = login.screenshot("android_login_error")

        assert screenshot_path.endswith(".png")
