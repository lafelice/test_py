import time
from selenium.webdriver.common.by import By


def test_entry_ad(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Entry Ad")
    element.click()
    time.sleep(1)

    # close pop-up
    browser.find_element(By.CSS_SELECTOR, ".modal-footer p").click()
    time.sleep(1)

    # restart with "Click here"
    browser.find_element(By.LINK_TEXT, "click here")
    assert "New Window" in browser.title

