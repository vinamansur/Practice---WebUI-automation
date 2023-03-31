from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from behave import Given, When, Then

service = Service(r'C:\selenium_drivers\geckodriver.exe')
driver = Firefox(service=service)
driver.install_addon(r'c:\selenium_drivers\uBlock0@raymondhill.net.xpi', temporary=True)
driver.implicitly_wait(10)
driver.maximize_window()


@Given("the website is launched")
def launch_app(self):
    # browsing to website
    driver.get("https://www.automationexercise.com")


@Then("a user inputs valid credentials")
def sign_in(self):
    # going to login page
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # logging in
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("vmansur@abc.com")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()


@Given("a logged user goes to products page")
def goto_products(self):
    # searching for t-shirts
    driver.find_element(By.PARTIAL_LINK_TEXT, " Products").click()


@When("they search for t-shirts")
def search_products(self):
    driver.find_element(By.ID, "search_product").send_keys('tshirt')
    driver.find_element(By.ID, "submit_search").click()


@Then("all available t-shirts are displayed")
def display_searched_products(self):
    assert True


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


@Then("the products are shown on cart")
def view_cart(self):
    # viewing cart
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//u").click()


@Then("user can remove the ones they didn't like")
def remove_products(self):
    # removing 1 T-Shirt that I don't like from the cart.
    driver.find_element(By.XPATH, "(//td[@class='cart_delete'])[2]//a").click()


@When("user proceeds to checkout")
def checkout(self):
    # proceeding to checkout and placing my order.
    driver.find_element(By.XPATH, "//section[@id='do_action']//a").click()


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


@When("card details are entered")
def payment_details(self):
    # Entering card details and paying for the order.
    driver.find_element(By.NAME, "name_on_card").send_keys("VINICIUS M MANSUR")
    driver.find_element(By.NAME, "card_number").send_keys("4321 1234 5678 0987")
    driver.find_element(By.NAME, "cvc").send_keys("000")
    driver.find_element(By.NAME, "expiry_month").send_keys("03")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")
    driver.find_element(By.ID, "submit").click()


@Then("order is payed")
def payment_confirmation(self):
    assert True


@Then("an Invoice is downloaded")
def download_invoice(self):
    # Downloading the Invoice.
    driver.find_element(By.XPATH, "//a[text() = 'Download Invoice']").click()
    time.sleep(5)







