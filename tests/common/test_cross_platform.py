"""
Cross-platform tests: the same test runs on both Android and iOS.
Uses pytest.mark.parametrize with the platform parameter.

Run:
    pytest tests/common/ --platform android   # Android only
    pytest tests/common/                      # both (requires both emulators running)
"""

import pytest

PLATFORMS = ["android", "ios"]


@pytest.mark.parametrize("platform", PLATFORMS)
def test_login_cross_platform(platform, request):
    """Valid login works the same on Android and iOS."""
    driver = request.getfixturevalue("driver")

    if platform == "android":
        from pages.android.login_page import LoginPage
        from pages.android.catalog_page import CatalogPage
    else:
        from pages.ios.login_page import LoginPage
        from pages.ios.catalog_page import CatalogPage

    login = LoginPage(driver)
    catalog = CatalogPage(driver)

    login.login("standard_user", "secret_sauce")
    assert catalog.is_loaded(), f"[{platform}] Catalog did not load after login"


@pytest.mark.parametrize("platform", PLATFORMS)
def test_error_message_cross_platform(platform, request):
    """Error message on login failure is consistent across platforms."""
    driver = request.getfixturevalue("driver")

    if platform == "android":
        from pages.android.login_page import LoginPage
    else:
        from pages.ios.login_page import LoginPage

    login = LoginPage(driver)
    login.login("wrong_user", "wrong_pass")

    error = login.get_error_message()
    assert "do not match" in error, f"[{platform}] Unexpected error message: {error}"
