from Workflows import example_workflows
from pages.ican_navigation import IcanNavigationMenu
from pytest_bdd import scenario, given, when, then


@scenario('tests.feature', 'user can navigate to the ican page')
def test_example_is_working_bdd():
    print('starting bdd test')


@given("an example site")
def goto_website(page):
    example_workflows.open_example_site_verify_page_load(page)


@when('they navigate to the ican website')
def navigate_to_ican(page):
    example_workflows.navigate_to_more_information_page_verify_menus(page)


@then('they are able to select all the menus')
def check_ican_nav_menu(page):
    ican_navigation = IcanNavigationMenu(page)
    ican_navigation.select_domains_link()
    ican_navigation.select_numbers_link()
    ican_navigation.select_protocols_link()
    ican_navigation.select_about_us_link()
