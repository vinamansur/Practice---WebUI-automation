from selenium.webdriver.common.by import By


def login(driver, context):
    # going to login page
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
    # logging in
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys(context.table[0]['email'])
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys(context.table[0]['password'])
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
    # checking if user is logged in
    assert driver.current_url == "https://www.automationexercise.com/", "Login error"