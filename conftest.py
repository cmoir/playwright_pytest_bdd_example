import pytest

from pathlib import Path

def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(".playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            page.screenshot(path=str(screenshot_dir / f"screenshot.png"))

def pytest_addoption(parser):
    parser.addoption('--menu-item', default='domains')
    parser.addoption('--expected-url', default='https://www.iana.org/domains')


@pytest.fixture
def menu_item(request):
    return request.config.getoption('--menu-item')


@pytest.fixture
def expected_url(request):
    return request.config.getoption('--expected-url')