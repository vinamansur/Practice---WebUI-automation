from selenium.webdriver.common.by import By


def check_cart(driver):
    # gets all products on cart to cart_list
    cart_list = driver.find_elements(By.XPATH, "//tr[contains(@id, 'product-')]")
    # checking if cart's empty
    assert len(cart_list) != 0, "Cart is empty!"
    # returning length of cart_list for later comparisons within test code
    return len(cart_list)


def remove_from_cart(driver, quantity):
    # getting cart list
    cart_list_1 = driver.find_elements(By.XPATH, "//tr[contains(@id, 'product-')]")
    # removing "quantity" products from cart, only if at least one product remains
    # otherwise, cart would get empty
    if len(cart_list_1) > quantity:
        for i in range(0, quantity):
            # index = len(cart_list_1) - i
            driver.find_element(By.XPATH, "(//td[@class='cart_delete'][last()]//a)").click()
    # checking products on cart after removal
    cart_list_2 = driver.find_elements(By.XPATH, "//tr[contains(@id, 'product-')]")
    # checking if removal was performed accordingly
    assert len(cart_list_2) == len(cart_list_1) - quantity, "products not removed properly from cart"


def checkout(driver):
    # proceeding to checkout and placing the order
    driver.find_element(By.XPATH, "//section[@id='do_action']//a").click()

