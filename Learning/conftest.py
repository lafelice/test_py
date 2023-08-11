import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    time.sleep(3)
    chrome_driver.quit()


@pytest.fixture
def test_check(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    yield browser
