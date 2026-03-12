"""
Tests cross-platform: el mismo test se ejecuta en Android e iOS.
Se usa pytest.mark.parametrize con la plataforma.

Ejecución:
    pytest tests/common/ --platform android   # solo Android
    pytest tests/common/                      # ambas (necesita ambos emuladores)
"""

import pytest


PLATFORMS = ["android", "ios"]


@pytest.mark.parametrize("platform", PLATFORMS)
def test_login_cross_platform(platform, request):
    """Login válido funciona igual en Android e iOS."""
    # Pedimos el driver con la plataforma correcta
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
    assert catalog.is_loaded(), f"[{platform}] El catálogo no cargó"


@pytest.mark.parametrize("platform", PLATFORMS)
def test_error_message_cross_platform(platform, request):
    """El mensaje de error de login es el mismo en ambas plataformas."""
    driver = request.getfixturevalue("driver")

    if platform == "android":
        from pages.android.login_page import LoginPage
    else:
        from pages.ios.login_page import LoginPage

    login = LoginPage(driver)
    login.login("wrong_user", "wrong_pass")

    error = login.get_error_message()
    assert "do not match" in error, f"[{platform}] Error inesperado: {error}"
