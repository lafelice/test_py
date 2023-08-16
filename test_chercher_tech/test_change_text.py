from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_change_text(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

    driver.find_element(By.ID, "populate-text").click()
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "h2")))
