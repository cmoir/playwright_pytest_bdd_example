from Workflows import example_workflows
from pages.ican_navigation import IcanNavigationMenu

def test_select_domains_link(page):
    ican_navigation = IcanNavigationMenu(page)

    example_workflows.launch_and_navigate_to_ican_page(ican_navigation, page)
    ican_navigation.click_domain_link()


def test_select_numbers_link(page):
    ican_navigation = IcanNavigationMenu(page)

    example_workflows.launch_and_navigate_to_ican_page(ican_navigation, page)
    ican_navigation.click_numbers_link()

def test_select_protocols_link(page):
    ican_navigation = IcanNavigationMenu(page)

    example_workflows.launch_and_navigate_to_ican_page(ican_navigation, page)
    ican_navigation.click_protocols_link()

def test_select_about_us_link(page):
    ican_navigation = IcanNavigationMenu(page)

    example_workflows.launch_and_navigate_to_ican_page(ican_navigation, page)
    ican_navigation.click_about_us_link()
