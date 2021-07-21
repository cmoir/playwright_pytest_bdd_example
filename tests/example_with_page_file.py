from page_file_example import main_page_pf as main_page


def test_example_is_working(page):
    page.goto("https://example.com")
    main_page.verify_header(page)
    main_page.select_more_information_link(page)
