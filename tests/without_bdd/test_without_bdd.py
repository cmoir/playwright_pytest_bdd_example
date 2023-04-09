from pages.main_page import MainPage
from pages.ican_navigation import IcanNavigationMenu

def test_select_domains_link(page):
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)

    page.goto("https://example.com")

    main_page.verify_header_text()
    main_page.select_more_information_link()
    ican_navigation.verify_menu_links()
    ican_navigation.click_domain_link()

def test_select_numbers_link(page):
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)

    page.goto("https://example.com")

    main_page.verify_header_text()
    main_page.select_more_information_link()
    ican_navigation.verify_menu_links()
    ican_navigation.click_numbers_link()

def test_select_protocols_link(page):
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)

    page.goto("https://example.com")

    main_page.verify_header_text()
    main_page.select_more_information_link()
    ican_navigation.verify_menu_links()
    ican_navigation.click_protocols_link()

def test_select_about_us_link(page):
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)

    page.goto("https://example.com")

    main_page.verify_header_text()
    main_page.select_more_information_link()
    ican_navigation.verify_menu_links()
    ican_navigation.click_about_us_link()
