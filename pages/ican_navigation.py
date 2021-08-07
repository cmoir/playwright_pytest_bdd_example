from playwright.sync_api import Page


class IcanNavigationMenu:
    def __init__(self, page: Page):
        self.page = page

    #Web Elements
    domains: str = "text=Domains"
    numbers: str = "text=Numbers"
    protocols: str = "text=Protocols"
    about_us: str = "text=About Us"

    def verify_menu_items(self):
        self.page.wait_for_selector(self.domains)
        self.page.wait_for_selector(self.numbers)
        self.page.wait_for_selector(self.protocols)
        self.page.wait_for_selector(self.about_us)

    def select_domains_link(self):
        with self.page.expect_navigation():
            self.page.click(self.domains)

    def select_numbers_link(self):
        with self.page.expect_navigation():
            self.page.click(self.numbers)

    def select_protocols_link(self):
        with self.page.expect_navigation():
            self.page.click(self.protocols)

    def select_about_us_link(self):
        with self.page.expect_navigation():
            self.page.click(self.about_us)