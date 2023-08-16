from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_display_button(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

    driver.find_element(By.CSS_SELECTOR, "#display-other-button").click()
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#hidden")))
