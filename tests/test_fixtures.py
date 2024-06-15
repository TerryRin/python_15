"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from pages.github_page import github_page


def test_github_desktop(setting_browser_desktop):
    github_page.open()
    github_page.desktop_button_sign_in()
    github_page.should_text_sign_in()

def test_github_mobile(setting_browser_mobile):
    github_page.open()
    github_page.mobile_button_sign_in()
    github_page.should_text_sign_in()