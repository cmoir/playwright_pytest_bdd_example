from playwright.sync_api import Page

#HTML Elements
header: str = 'h1'
more_info_link: str = 'text=More information'


def verify_header(page: Page):
    assert page.inner_text(header) == 'Example Domain'


def select_more_information_link(page: Page):
    with page.expect_navigation():
        page.click(more_info_link)
