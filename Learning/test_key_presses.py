import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_key_presses(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Key Presses")
    element.click()
    time.sleep(1)


    browser.find_element(By.ID, "target").send_keys(Keys.TAB)
    time.sleep(2)
    result = browser.find_element(By.ID, "result")

    assert "You entered: TAB" in result.text
