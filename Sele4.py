from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")   # Demo site for Radio buttons
time.sleep(2)

# Select Radio Button
radio_button = driver.find_element(By.ID, "yesRadio")
radio_button.click()
time.sleep(2)

print("Radio Selected:", radio_button.is_selected())
print("Radio Displayed:", radio_button.is_displayed())
print("Radio Enabled:", radio_button.is_enabled())

# Open CheckBox demo site
driver.get("https://demoqa.com/checkbox")
time.sleep(2)

# Select CheckBox
checkbox = driver.find_element(By.CLASS_NAME, "rct-checkbox")
checkbox.click()
time.sleep(2)

print("Checkbox Selected:", checkbox.is_selected())
print("Checkbox Displayed:", checkbox.is_displayed())
print("Checkbox Enabled:", checkbox.is_enabled())

time.sleep(20)
driver.quit()
