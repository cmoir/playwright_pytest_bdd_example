from page_file_example import main_page_pf as main_page
from page_file_example import ican_navigation as ican_navigation


def test_example_is_working(page):
    page.goto("https://example.com")
    main_page.verify_header(page)
    main_page.select_more_information_link(page)
    ican_navigation.verify_menu_items(page)
    ican_navigation.select_domains_link(page)
    ican_navigation.select_numbers_link(page)
    ican_navigation.select_protocols_link(page)
    ican_navigation.select_about_us_link(page)
