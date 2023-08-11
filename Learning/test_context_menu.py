from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_context_menu(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")

    element = browser.find_element(By.LINK_TEXT, "Context Menu")
    element.click()

    box = browser.find_element(By.ID, "hot-spot")
    action = webdriver.ActionChains(browser)
    action.context_click(box).perform()

    alert = Alert(browser)
    alert_text = alert.text
    assert "You selected a context menu" in alert_text
