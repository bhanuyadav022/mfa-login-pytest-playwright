import pytest
from pages.index_page import IndexPage
from utilities.config_manager import ConfigManager

config_data = ConfigManager.read_config()

def test_login_page_valid_credentials(login_page, signup_page):
    login_page.enter_login_credentials(config_data['user'], config_data['password'], signup_page)
    login_page.submit_form()
    index_page = IndexPage(login_page.page, config_data["base_url"])

    assert index_page.get_title() == 'Welcome!'

def test_login_with_all_empty_value(login_page):
    login_page.enter_login_credentials("", "", "")
    login_page.submit_form()

    assert login_page.show_error_message() == "The Username is Required!" 

def test_login_with_empty_password (login_page, signup_page):
    login_page.enter_login_credentials(config_data['user'], "", signup_page)
    login_page.submit_form()

    assert login_page.show_error_message() == "The Password is Required!" 

def test_login_with_empty_username (login_page, signup_page):
    login_page.enter_login_credentials("", config_data['password'], signup_page)
    login_page.submit_form()

    assert login_page.show_error_message() == "The Password is Required!" 

def test_login_with_empty_password (login_page, signup_page):
    login_page.enter_login_credentials(config_data['user'], "", signup_page)
    login_page.submit_form()

    assert login_page.show_error_message() == "The Password is Required!" 
