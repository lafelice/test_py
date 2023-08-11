from selenium.webdriver.common.by import By


def test_form_authentication(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Form Authentication")
    element.click()

    # Locate the username and password fields and enter credentials
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_button.click()

    # Verify the success message
    success_message = browser.find_element(By.XPATH, "//div[@id='flash']")
    assert "You logged into a secure area!" in success_message.text
