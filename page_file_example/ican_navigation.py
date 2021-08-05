from playwright.sync_api import Page

# Web Elements
domains: str = "text=Domains"
numbers: str = "text=Numbers"
protocols: str = "text=Protocols"
about_us: str = "text=About Us"


def verify_menu_items(page):
    page.wait_for_selector(domains)
    page.wait_for_selector(numbers)
    page.wait_for_selector(protocols)
    page.wait_for_selector(about_us)


def select_domains_link(page):
    with page.expect_navigation():
        page.click(domains)


def select_numbers_link(page):
    with page.expect_navigation():
        page.click(numbers)


def select_protocols_link(page):
    with page.expect_navigation():
        page.click(protocols)


def select_about_us_link(page):
    with page.expect_navigation():
        page.click(about_us)
