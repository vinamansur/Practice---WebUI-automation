from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from behave import Given, When, Then

service = Service(r'C:\selenium_drivers\geckodriver.exe')
driver = Firefox(service=service)
driver.install_addon(r'c:\selenium_drivers\uBlock0@raymondhill.net.xpi', temporary=True)
driver.implicitly_wait(5)
driver.maximize_window()


@Given("the website is launched")
def launch_app(self):
    # browsing to website
    driver.get("https://www.automationexercise.com")
    # checking if the right website has loaded on browser
    assert driver.title == "Automation Exercise", "website did not load properly"


@Then("a user logs in with valid credentials")
def sign_in(self):
    # going to login page
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # logging in
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("vmansur@abc.com")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
    # checking if user is logged in
    assert driver.current_url == "https://www.automationexercise.com/", "Login error"


@Given("a logged user goes to products page")
def goto_products(self):
    # searching for t-shirts
    driver.find_element(By.PARTIAL_LINK_TEXT, " Products").click()
    # checking if the right page is being shown
    assert driver.title == "Automation Exercise - All Products"


@When("they search for t-shirts")
def search_products(self):
    driver.find_element(By.ID, "search_product").send_keys('tshirt')
    driver.find_element(By.ID, "submit_search").click()
    # checking if the right page is being shown
    assert driver.find_element(By.XPATH, "//h2[contains(text(), 'Searched Products')]").is_displayed()


@When("two t-shirts are added to cart")
def add_products(self):
    # ------ adding the first t-shirt to cart -----------
    # scrolling to the element, before clicking
    driver.execute_script("arguments[0].scrollIntoView(true)",
                          driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]"))
    driver.execute_script("window.scrollBy(0,-500)", "")
    # selecting the first option
    driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]").click()
    # clicking "Add to cart"
    driver.find_element(By.XPATH, "//div[@class='product-information']//button").click()

    # checking if first product was actually added to cart
    time.sleep(0.5)  # waiting for the modal window to show up
    assert driver.find_element(By.XPATH, "//h4[contains(text(), 'Added!')]")

    # returning to search results
    driver.back()
    # ------ adding the second t-shirt to cart -----------
    # scrolling to the element, before clicking
    driver.execute_script("arguments[0].scrollIntoView(true)",
                          driver.find_element(By.XPATH, "(//a[text()='View Product'])[2]"))
    driver.execute_script("window.scrollBy(0,-500)", "")
    # selecting the second option
    driver.find_element(By.XPATH, "(//a[text()='View Product'])[2]").click()
    # clicking "Add to cart"
    driver.find_element(By.XPATH, "//div[@class='product-information']//button").click()

    # checking if first product was actually added to cart
    time.sleep(0.5)  # waiting for the modal window to show up
    assert driver.find_element(By.XPATH, "//h4[contains(text(), 'Added!')]")


@Then("the products are shown on cart")
def view_cart(self):
    # viewing cart
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//u").click()
    # checking if there are two products on cart
    products = driver.find_elements(By.XPATH, "//tr[contains(@id, 'product-')]")
    assert len(products) == 2, "Cart doesn't contain two products"


@Then("user can remove the ones they didn't like")
def remove_products(self):
    # removing 1 T-Shirt that I don't like from the cart
    driver.find_element(By.XPATH, "(//td[@class='cart_delete'])[2]//a").click()
    # checking it there's only one product on cart
    products = driver.find_elements(By.XPATH, "//tr[contains(@id, 'product-')]")
    assert len(products) == 1, "Cart contains more than one product"


@When("user proceeds to checkout")
def checkout(self):
    # proceeding to checkout and placing my order
    driver.find_element(By.XPATH, "//section[@id='do_action']//a").click()
    # checking if user is on checkout page
    assert driver.title == "Automation Exercise - Checkout", "user is not on checkout page"


@Then("they can review the order")
def order_review(self):
    driver.execute_script("arguments[0].scrollIntoView(true)",
                          driver.find_element(By.XPATH, "//h2[contains(text(), 'Review Your Order')]"))
    driver.find_element(By.XPATH, "//textarea").send_keys("Thank you!")
    driver.execute_script("arguments[0].scrollIntoView(true)",
                          driver.find_element(By.XPATH, "//h2[contains(text(), 'Review Your Order')]"))


@Then("proceed to payment")
def goto_payment(self):
    driver.find_element(By.XPATH, "//a[@href='/payment']").click()
    # checking if user is on payment page
    assert driver.title == "Automation Exercise - Payment", "user is not on payment page"


@When("payment is completed")
def payment_details(self):
    # Entering card details and paying for the order
    driver.find_element(By.NAME, "name_on_card").send_keys("VINICIUS M MANSUR")
    driver.find_element(By.NAME, "card_number").send_keys("4321 1234 5678 0987")
    driver.find_element(By.NAME, "cvc").send_keys("000")
    driver.find_element(By.NAME, "expiry_month").send_keys("03")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")
    driver.find_element(By.ID, "submit").click()


@Then("order is confirmed")
def payment_confirmation(self):
    assert driver.find_element(By.XPATH, "//h2[@data-qa='order-placed']")


@Then("an invoice is downloaded")
def download_invoice(self):
    # Downloading the Invoice
    download_invoice_button = driver.find_element(By.XPATH, "//a[text() = 'Download Invoice']")
    # check if download button is enabled before clicking on it
    assert download_invoice_button.is_enabled()
    download_invoice_button.click()
