from selenium import webdriver
import pytest


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver


def pytest_addoption(parser):  # read form cli
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

