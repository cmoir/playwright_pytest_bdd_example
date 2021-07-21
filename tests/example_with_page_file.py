from page_file_example import main_page_pf


def test_example_is_working(page):
    page.goto("https://example.com")
    main_page_pf.check_header(page)
    main_page_pf.select_more_information_link(page)
