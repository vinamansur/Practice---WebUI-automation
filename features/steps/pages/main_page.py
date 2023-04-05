from selenium.webdriver.common.by import By

def launch_website(driver):
    driver.get("https://www.automationexercise.com")
    # checking if the right website has loaded on browser
    assert driver.title == "Automation Exercise", "website did not load properly"

def go_to_products(driver):
    # searching for t-shirts
    driver.find_element(By.PARTIAL_LINK_TEXT, " Products").click()
    # checking if the right page is being shown
    assert driver.title == "Automation Exercise - All Products"