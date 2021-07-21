This example project uses the pytest-playwright project as it base.

https://github.com/microsoft/playwright-pytest
pip install pytest-playwright

Docs
https://playwright.dev/python/docs/intro


In both examples use the sync_api.


In this example project there are two examples.
The 'example_with_page_object' test is using a standard page object model, where the selectors 
and functions are inside a class.

The 'example_with_page_file' test is using the same concept but using files to group the pages without the class structure.
This simpler implementation that works just as well and is easier to implement. 