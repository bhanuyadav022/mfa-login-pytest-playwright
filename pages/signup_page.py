from pages.base_page import BasePage
from data.locator import signup_locators

class SignupPage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

        
    def navigate_url(self):
        self.navigate("/signup")

    def set_totpcode(self):
        return self.get_element_content(signup_locators['totpcde'])
    
