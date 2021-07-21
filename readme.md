##Playwright Python Example Poject
- Depends on [pytest-playwright](https://github.com/microsoft/playwright-pytest) 
- pip install pytest-playwright

## Playwright Documentation

[https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)


## Example Overview
- There are two example formats
- Both examples use the sync_api.

## Page Object example
This test is using a standard page object model, where the selectors 
and functions are inside a class.

```python
class MainPage:
    def __init__(self, page: Page):
        self.page = page

    #web Elements
    header: str = 'h1'
    more_info_link: str = 'text=More information'

    def verify_header(self):
        assert self.page.inner_text(self.header) == 'Example Domain'

    def select_more_information_link(self):
        self.page.click(self.more_info_link)
```

## Page File example
This test is using the same concept but using files to group the pages without the class structure.
This simpler implementation that works just as well and is easier to implement.

```python
header: str = 'h1'
more_info_link: str = 'text=More information'


def verify_header(page: Page):
    assert page.inner_text(header) == 'Example Domain'


def select_more_information_link(page: Page):
    page.click(more_info_link)
```