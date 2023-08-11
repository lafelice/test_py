import time
from selenium.webdriver.common.by import By


def test_frames(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Frames")
    element.click()

    # navigate to iFrame and type the text
    browser.find_element(By.LINK_TEXT, "iFrame").click()
    time.sleep(1)
    browser.switch_to.frame("mce_0_ifr")
    browser.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Slava Ukraini!")
