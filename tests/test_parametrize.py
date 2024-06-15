"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest

from pages.github_page import github_page


@pytest.mark.parametrize('driver', ['desktop'], indirect=True)
def test_github_desktop(driver):
    github_page.open()
    github_page.desktop_button_sign_in()
    github_page.should_text_sign_in()

@pytest.mark.parametrize('driver', ['mobile'], indirect=True)
def test_github_mobile(driver):
    github_page.open()
    github_page.mobile_button_sign_in()
    github_page.should_text_sign_in()
