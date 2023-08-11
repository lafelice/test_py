import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_horizontal_slider(browser):
    browser.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    # open link
    element = browser.find_element(By.LINK_TEXT, "Horizontal Slider")
    element.click()

    slider = browser.find_element(By.CSS_SELECTOR, ".sliderContainer input")

    action = ActionChains(browser)
    action.drag_and_drop_by_offset(slider, 50, 0).perform()
    time.sleep(1)
    assert "4.5" in browser.find_element(By.ID, "range").text

    current_value = float(slider.get_attribute("value"))
    target_value = 3
    arrow_presses = int((current_value - target_value) * 2)  # Assuming each press changes by 0.5

    for _ in range(arrow_presses):
        slider.send_keys(Keys.ARROW_LEFT)
       
