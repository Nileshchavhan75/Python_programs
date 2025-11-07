from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Using text()
driver.find_element(By.XPATH, "//label[text()='Username']").click()

# Using contains()
driver.find_element(By.XPATH, "//input[contains(@id,'username')]").send_keys("student")

# Using AND operator
driver.find_element(By.XPATH, "//input[@type='password' and contains(@id,'password')]").send_keys("Password123")

driver.find_element(By.XPATH, "//button[@id='submit' and @type='submit']").click()

print("Dynamic XPath (text, contains, and) executed successfully!")

time.sleep(10)   # keeps the browser open for 10 seconds
driver.quit()
