from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()
driver.get("https://example.com")

# Dynamic XPaths examples
driver.find_element(By.XPATH, "//h1[text()='Example Domain']")  # by text
driver.find_element(By.XPATH, "//a[contains(text(),'More')]")    # contains
driver.find_element(By.XPATH, "//input[@type='text' and @name='username']")  # AND condition

input("Press Enter to close the browser...")  # waits until you press Enter

driver.quit()
