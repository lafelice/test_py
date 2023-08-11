from selenium.webdriver.common.by import By


def test_input(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Inputs")
    element.click()

    browser.find_element(By.CSS_SELECTOR, "input").send_keys("88")
