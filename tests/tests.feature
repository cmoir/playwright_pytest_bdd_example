# Updated feature file

Feature: Example BDD tests

    Scenario: user can navigate to the domains page
        Given an example site
        When they click on the "More information" link
        Then they are able to navigate to the Domains page

    Scenario: user can navigate to the ican page
        Given an example site
        When they click on the "More information" link
        Then they are able to navigate to the expected web page

        Examples:
        | menu_item | expected_url                  |
        | domains  | https://www.iana.org/domains   |
        | numbers  | https://www.iana.org/numbers   |
        | protocols | https://www.iana.org/protocols |
        | about us | https://www.iana.org/about     |
