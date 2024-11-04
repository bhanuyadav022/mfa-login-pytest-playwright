from pages.base_page import BasePage
from data.locator import login_locators
class LoginPage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        
    def navigate_url(self):
        self.navigate("/login")

    def set_username(self, username):
        self.fill_field(login_locators['username'], username)

    def set_password(self, password):
        self.fill_field(login_locators['password'], password)

    def set_totp(self, totp):
        self.fill_field(login_locators['mfa'], totp)

    def enter_login_credentials (self, username, password, totp):
        self.set_username(username)
        self.set_password(password)
        self.set_totp(totp)

    def submit_form(self):
        self.click_element(login_locators['sign_in'])

    def show_error_message(self):
        return self.get_element_content(login_locators['error_msg'])
