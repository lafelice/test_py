from selenium.webdriver.common.by import By


def test_navigate_to_url(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    assert "The Internet" in browser.title


def test_checkbox(browser):
    element = browser.find_element(By.LINK_TEXT, "Checkboxes")
    element.click()

    checkbox_1 = browser.find_element(By.XPATH, "//input[@type='checkbox'][1]").click()
    checkbox_2 = browser.find_element(By.XPATH, "//input[@type='checkbox'][2]").click()
    print(checkbox_2, checkbox_1)
