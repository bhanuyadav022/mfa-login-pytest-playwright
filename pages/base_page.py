class BasePage:

    def __init__(self, page, base_url):
        self.base_url = base_url
        self.page = page

    def navigate(self, endpoint):
        self.page.goto(self.base_url+endpoint)

    def fill_field(self, selector, username):
        self.page.locator(selector).fill(username)

    def get_element_content(self, selector):
        return self.page.locator(selector).text_content()

    def click_element(self, selector):
        self.page.locator(selector).click()

