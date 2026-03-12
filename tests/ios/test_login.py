"""Login tests — iOS."""

import pytest
from pages.ios.login_page import LoginPage
from pages.ios.catalog_page import CatalogPage

pytestmark = pytest.mark.platform("ios")


class TestLoginIOS:

    def test_login_valid_credentials(self, driver):
        login = LoginPage(driver)
        catalog = CatalogPage(driver)
        login.login("standard_user", "secret_sauce")
        assert catalog.is_loaded(), "Catalog did not load after valid login on iOS"

    def test_login_invalid_credentials(self, driver):
        login = LoginPage(driver)
        login.login("standard_user", "bad_pass")
        assert "do not match" in login.get_error_message()

    def test_login_empty_username(self, driver):
        login = LoginPage(driver)
        login.type_text(login.PASSWORD_FIELD, "secret_sauce")
        login.click(login.LOGIN_BUTTON)
        assert login.is_username_error_shown()

    def test_login_screenshot(self, driver):
        login = LoginPage(driver)
        login.login("bad", "bad")
        path = login.screenshot("ios_login_error")
        assert path.endswith(".png")
