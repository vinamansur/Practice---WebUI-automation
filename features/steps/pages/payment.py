from selenium.webdriver.common.by import By


def pay_order(driver):
    # Entering card details and paying for the order
    driver.find_element(By.NAME, "name_on_card").send_keys("VINICIUS M MANSUR")
    driver.find_element(By.NAME, "card_number").send_keys("4321 1234 5678 0987")
    driver.find_element(By.NAME, "cvc").send_keys("000")
    driver.find_element(By.NAME, "expiry_month").send_keys("03")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")
    driver.find_element(By.ID, "submit").click()
