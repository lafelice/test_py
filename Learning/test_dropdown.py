from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")

    element = browser.find_element(By.LINK_TEXT, "Dropdown")
    element.click()

    dropdown = browser.find_element(By.CSS_SELECTOR, ".example #dropdown")
    select = Select(dropdown)
    select.select_by_value("2")
    header = browser.find_element(By.CSS_SELECTOR, "body h3")
    assert "Dropdown List" in header.text
