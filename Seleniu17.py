from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch the Chrome browser
driver = webdriver.Chrome()

# Open a web page
driver.get("https://www.example.com")   # You can replace with any website
driver.maximize_window()
print("Opened website successfully.")

# Wait for page to load
time.sleep(2)

# ----- 1️⃣ Capture Full Page Screenshot -----
driver.save_screenshot("full_page.png")
print("✅ Full page screenshot saved as 'full_page.png'")

# ----- 2️⃣ Capture Screenshot of Specific Element -----
element = driver.find_element(By.TAG_NAME, "h1")   # Captures the first <h1> tag
element.screenshot("element_screenshot.png")
print("✅ Element screenshot saved as 'element_screenshot.png'")

# Close the browser
driver.quit()
print("🚀 Screenshot handling demo completed successfully!")
