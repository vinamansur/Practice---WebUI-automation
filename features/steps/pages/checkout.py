from selenium.webdriver.common.by import By


def review_order(driver):
    driver.execute_script("arguments[0].scrollIntoView(true)",
                          driver.find_element(By.XPATH, "//h2[contains(text(), 'Review Your Order')]"))
    driver.find_element(By.XPATH, "//textarea").send_keys("Thank you!")
    driver.execute_script("arguments[0].scrollIntoView(true)",
                          driver.find_element(By.XPATH, "//h2[contains(text(), 'Review Your Order')]"))


def place_order(driver):
    driver.find_element(By.XPATH, "//a[@href='/payment']").click()
