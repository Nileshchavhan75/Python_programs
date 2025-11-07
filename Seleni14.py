from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open a sample login page (demo site)
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Use dynamic XPaths
driver.find_element(By.XPATH, "//input[contains(@id,'username')]").send_keys("student")
driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("Password123")
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

print("✅ Login Successful using Dynamic XPath!")
time.sleep(5)
driver.quit()