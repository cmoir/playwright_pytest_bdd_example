from playwright.sync_api import Page


class IcanNavigationMenu:
    DOMAIN_LINK = 'text=Domains'
    NUMBERS_LINK = 'text=Numbers'
    PROTOCOLS_LINK = 'text=Protocols'
    ABOUT_US_LINK = 'text=About Us'

    def __init__(self, page: Page):
        self.page = page

    def verify_menu_links(self):
        self.page.wait_for_selector(self.DOMAIN_LINK)
        self.page.wait_for_selector(self.NUMBERS_LINK)
        self.page.wait_for_selector(self.PROTOCOLS_LINK)
        self.page.wait_for_selector(self.ABOUT_US_LINK)

    def click_domain_link(self):
        with self.page.expect_navigation():
            self.page.click(self.DOMAIN_LINK)

    def click_numbers_link(self):
        with self.page.expect_navigation():
            self.page.click(self.NUMBERS_LINK)

    def click_protocols_link(self):
        with self.page.expect_navigation():
            self.page.click(self.PROTOCOLS_LINK)

    def click_about_us_link(self):
        with self.page.expect_navigation():
            self.page.click(self.ABOUT_US_LINK)

