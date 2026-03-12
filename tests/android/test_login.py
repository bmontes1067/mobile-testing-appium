"""
Login tests — Android
Valid credentials for My Demo App (Sauce Labs):
  - standard_user / secret_sauce
  - locked_out_user / secret_sauce  (blocked user)
"""

import pytest
from pages.android.login_page import LoginPage
from pages.android.catalog_page import CatalogPage

pytestmark = pytest.mark.platform("android")


class TestLoginAndroid:

    def test_login_valid_credentials(self, driver):
        """Login with valid credentials navigates to the catalog."""
        login = LoginPage(driver)
        catalog = CatalogPage(driver)

        login.login("standard_user", "secret_sauce")

        assert catalog.is_loaded(), "Catalog did not load after valid login"

    def test_login_invalid_password(self, driver):
        """Wrong password shows an error message."""
        login = LoginPage(driver)

        login.login("standard_user", "wrong_password")

        assert "do not match" in login.get_error_message()

    def test_login_empty_username(self, driver):
        """Empty username shows a required field error."""
        login = LoginPage(driver)

        login.enter_password("secret_sauce")
        login.tap_login()

        assert login.is_username_error_shown(), "Username required error not shown"

    def test_login_empty_password(self, driver):
        """Empty password shows a required field error."""
        login = LoginPage(driver)

        login.enter_username("standard_user")
        login.tap_login()

        assert login.is_password_error_shown(), "Password required error not shown"

    def test_login_both_fields_empty(self, driver):
        """Submitting empty form shows username error."""
        login = LoginPage(driver)

        login.tap_login()

        assert login.is_username_error_shown()

    def test_login_locked_user(self, driver):
        """Locked out user sees an error message."""
        login = LoginPage(driver)

        login.login("locked_out_user", "secret_sauce")

        error = login.get_error_message()
        assert "locked out" in error.lower() or "do not match" in error.lower()

    def test_login_screenshot_on_error_state(self, driver):
        """Verifies error state is captured correctly in a screenshot."""
        login = LoginPage(driver)

        login.login("bad_user", "bad_pass")
        screenshot_path = login.screenshot("android_login_error")

        assert screenshot_path.endswith(".png")
