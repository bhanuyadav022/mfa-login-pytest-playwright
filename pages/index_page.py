from pages.base_page import BasePage
from data.locator import index_locators


class IndexPage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    def navigate_url(self):
        self.navigate("/")

    def get_title(self):
        return self.get_element_content(index_locators['title_element'])

    def should_have_title(self, value):
        expected_title = self.page.locator("h1").text_content()
        if expected_title == value:
            return True
        else:
            return False
