## Playwright Python pytest_bdd example
- Depends on [pytest-playwright](https://github.com/microsoft/playwright-pytest) 
- pip install pytest-playwright
- pip install pytest-bdd
- install playwright

## Playwright Documentation

[https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)

## pytest-bdd Documentation

See [https://pypi.org/project/pytest-bdd/](https://pypi.org/project/pytest-bdd/) for reporting options.
 


## Page Object example
This test is using a standard page object model, where the selectors 
and functions are group inside a class.

Example is given with and without the bdd layer

Alternative format that uses files instead of objects to group the pages can be found
[here](https://github.com/cmoir/playwright-pytest-pagefile-example)

## Recommended plugins:
pytest-xdist - used to run multiple tests at the same time
pytest-html - for nice simple html report

