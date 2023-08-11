import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_hovers(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Hovers")
    element.click()

    image = browser.find_element(By.XPATH, "(//div[@class='figure'])[2]")
    action = ActionChains(browser)
    action.move_to_element(image).perform()
    time.sleep(1)
    browser.find_element(By.LINK_TEXT, "View profile").click()

    assert "Not Found" in browser.page_source
