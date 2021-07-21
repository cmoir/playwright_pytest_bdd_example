from pages_object_example.main_page import MainPage


def test_example_is_working(page):
    page.goto("https://example.com")
    main_page = MainPage(page)
    main_page.check_header()
    main_page.select_more_information_link()
