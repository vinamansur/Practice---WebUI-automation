from selenium.webdriver.common.by import By

def find_products(driver, product):
    driver.find_element(By.ID, "search_product").send_keys(product)
    driver.find_element(By.ID, "submit_search").click()
    # checking if the right page is being shown
    assert driver.find_element(By.XPATH, "//h2[contains(text(), 'Searched Products')]").is_displayed()

def add_to_cart(driver, quantity):
    # stores all products (button elements) returned from search on search_list
    search_list = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']//a")
    # loops through first "qty" products in the list, unless list contains less than "qty" products
    # clicks on "Add to cart", then "Continue Shopping"
    num_products = min(len(search_list), quantity)
    for i in range(0, num_products):
        search_list[i].click()
        driver.find_element(By.XPATH, "//div[@class='modal-footer']//button").click()
    # viewing cart
    driver.find_element(By.PARTIAL_LINK_TEXT, "Cart").click()
    # returning num_products for later comparisons within test code
    return num_products
