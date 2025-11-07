from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# Dropdown example
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
driver.switch_to.frame("iframeResult")
Select(driver.find_element(By.ID, "cars")).select_by_visible_text("Saab")
print("Selected from dropdown: Saab")
driver.switch_to.default_content()

# List example using dynamic XPath
driver.get("https://www.w3schools.com/html/html_lists.asp")
for i, item in enumerate(driver.find_elements(By.XPATH, "//ul[1]/li"), 1):
    print(f"{i}. {item.text}")

# Execute JavaScript
driver.execute_script("alert('JavaScript executed successfully!')")
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(5)
driver.quit()
