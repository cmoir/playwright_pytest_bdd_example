from pages.main_page import MainPage
from pages.ican_navigation import IcanNavigationMenu


def open_example_site_verify_page_load(page):
    main_page = MainPage(page)
    page.goto("https://example.com")
    main_page.verify_header_text()

def navigate_to_more_information_page_verify_menus(page):
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)
    main_page.select_more_information_link()
    ican_navigation.verify_menu_links()

def launch_and_navigate_to_ican_page(ican_navigation, page):
    open_example_site_verify_page_load(page)
    navigate_to_more_information_page_verify_menus(page)



