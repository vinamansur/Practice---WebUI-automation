from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# getting Selenium driver for MS Edge
driver = webdriver.Edge(service=Service(r"c:\selenium_drivers\msedgedriver.exe"))

driver.implicitly_wait(10)

# browsing to website
driver.get("https://www.automationexercise.com")

# going to login page
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# logging in
driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("vmansur@abc.com")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

# searching for t-shirts
driver.find_element(By.PARTIAL_LINK_TEXT, " Products").click()
# driver.find_element(By.XPATH, "//a[@href= '/products']").click()
driver.find_element(By.ID, "search_product").send_keys('tshirt')
driver.find_element(By.ID, "submit_search").click()

# ------ adding the first t-shirt to cart -----------
# scrolling to the element, before clicking
ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]")).perform()
# selecting the first option
driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]").click()
# clicking "Add to cart"
driver.find_element(By.XPATH, "//div[@class='product-information']//button").click()
#returning to search results
driver.find_element(By.XPATH, "//div[@class='modal-footer']//button").click()
driver.back()

# ------ adding the second t-shirt to cart -----------
# scrolling to the element, before clicking
ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//a[text()='View Product'])[2]")).perform()
# selecting the second option
driver.find_element(By.XPATH, "(//a[text()='View Product'])[2]").click()
# clicking "Add to cart"
driver.find_element(By.XPATH, "//div[@class='product-information']//button").click()

# viewing cart
driver.find_element(By.XPATH, "//div[@class='modal-body']//a").click()

# removing 1 T-Shirt that I don't like from the cart.
driver.find_element(By.XPATH, "(//td[@class='cart_delete'])[2]//a").click()

# proceeding to checkout and placing my order.
driver.find_element(By.XPATH, "//section[@id='do_action']//a").click()
ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//a[@href='/payment']")).perform()
driver.find_element(By.XPATH, "//textarea").send_keys("Thank you!")
driver.find_element(By.XPATH, "//a[@href='/payment']").click()

# Entering card details and paying for the order.


# Downloading the Invoice.