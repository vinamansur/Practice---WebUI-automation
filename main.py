from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# getting Selenium driver for MS Edge
driver = webdriver.Edge(service=Service(r"c:\selenium_drivers\msedgedriver.exe"))

# browsing to website
driver.get("https://www.automationexercise.com")

# going to login page
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# logging in
driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("vmansur@abc.com")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
