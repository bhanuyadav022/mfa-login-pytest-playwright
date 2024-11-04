import pytest
from playwright.sync_api import sync_playwright
from utilities.config_manager import ConfigManager
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


config_data = ConfigManager.read_config()


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def login_page(browser):
    page = browser.new_page()
    login_page = LoginPage(page, config_data["base_url"])
    login_page.navigate_url()
    yield login_page
    page.close()


@pytest.fixture(scope="function")
def signup_page(browser):
    page = browser.new_page()
    signup_page = SignupPage(page, config_data["base_url"])
    signup_page.navigate_url()
    code = signup_page.set_totpcode()
    page.close()
    return code
