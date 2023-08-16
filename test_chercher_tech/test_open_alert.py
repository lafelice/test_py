from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_open_alert(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

    driver.find_element(By.CSS_SELECTOR, "#alert.btn.btn-success").click()
    wait = WebDriverWait(driver, 10)

    wait.until(EC.alert_is_present())
