from selenium.webdriver.common.by import By


def get_invoice(driver):
    # Downloading the Invoice
    download_invoice_button = driver.find_element(By.XPATH, "//a[text() = 'Download Invoice']")
    # check if download button is enabled before clicking on it
    assert download_invoice_button.is_enabled(), "unable to download the invoice"
    download_invoice_button.click()
