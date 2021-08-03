from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    #Web Elements
    header: str = 'h1'
    more_info_link: str = 'text=More information'

    def verifiy_header(self):
        assert self.page.inner_text(self.header) == 'Example Domain'

    def select_more_information_link(self):
        with self.page.expect_navigation():
            self.page.click(self.more_info_link)