from page_object_example.main_page_pom import MainPage


def test_example_is_working(page):
    page.goto("https://example.com")
    main_page = MainPage(page)
    main_page.verifiy_header()
    main_page.select_more_information_link()
