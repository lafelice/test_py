from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_enable_button(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

    driver.find_element(By.CSS_SELECTOR, "#enable-button").click()
    wait = WebDriverWait(driver, 15)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#disable"))).click()
