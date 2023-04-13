from pages import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from behave import Given, When, Then
import logging

service = Service(r'C:\selenium_drivers\geckodriver.exe')
driver = Firefox(service=service)
driver.install_addon(r'c:\selenium_drivers\uBlock0@raymondhill.net.xpi', temporary=True)
driver.implicitly_wait(5)
driver.maximize_window()

# Create and configure logger
logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s', filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


@Given("the website is launched")
def launch_app(self):
    logger.info("Launching the website")
    main_page.launch_website(driver)


@ Then('a user logs in with valid credentials')
def sign_in(context):
    logger.info("Logging in...")
    login.login(driver, context)


@Given("a logged user goes to products page")
def goto_products(self):
    logger.info("Browsing to main page")
    main_page.go_to_products(driver)


@When('they search for "{product}"')
def search_products(self, product):
    logger.info("searching for " + product)
    products.find_products(driver, product)


@When('"{qty_to_add}" products are added to cart')
def add_products(self, qty_to_add):
    # adding products to cart, storing number of products added
    logger.info("adding " + qty_to_add + " product(s) to cart")
    qty_added = products.add_to_cart(driver, int(qty_to_add))
    # checking the cart
    qty_on_cart = cart.check_cart(driver)
    # checking if products were added properly to cart
    logger.info("checking if there's " + qty_to_add + " products on cart")
    assert qty_added == qty_on_cart, "products were not added correctly to cart"


@Then('user removes "{qty_to_remove}" product that they did not like')
def remove_products(self, qty_to_remove):
    logger.info("removing " + qty_to_remove + " product(s) to cart")
    cart.remove_from_cart(driver, int(qty_to_remove))
    # checking if user is on checkout page
    assert driver.title == "Automation Exercise - Checkout", "user is not on checkout page"


@When("user proceeds to checkout")
def proceed_to_checkout(self):
    # proceeding to checkout and placing the order
    logger.info("checking out")
    cart.checkout(driver)
    # checking if user is on checkout page
    assert driver.title == "Automation Exercise - Checkout", "user is not on checkout page"


@Then("they can review the order")
def order_review(self):
    logger.info("reviewing the order")
    checkout.review_order(driver)


@Then("proceed to payment")
def goto_payment(self):
    # driver.find_element(By.XPATH, "//a[@href='/payment']").click()
    logger.info("placing the order")
    checkout.place_order(driver)
    # checking if user is on payment page
    assert driver.title == "Automation Exercise - Payment", "user is not on payment page"


@When("payment is completed")
def payment_details(self):
    logger.info("Entering payment details")
    payment.pay_order(driver)


@Then("order is confirmed")
def payment_confirmation(self):
    logger.info("confirming the order")
    assert driver.find_element(By.XPATH, "//h2[@data-qa='order-placed']")


@Then("an invoice is downloaded")
def download_invoice(self):
    logger.info("downloading the invoice")
    final_page.get_invoice(driver)
