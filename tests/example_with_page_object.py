from page_object_example.main_page_pom import MainPage
from page_object_example.ican_navigation import IcanNavigationMenu

def test_example_is_working(page):
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)

    page.goto("https://example.com")

    main_page.verifiy_header()
    main_page.select_more_information_link()
    ican_navigation.verify_menu_items()
    ican_navigation.select_domains_link()
    ican_navigation.select_numbers_link()
    ican_navigation.select_protocols_link()
    ican_navigation.select_about_us_link()

