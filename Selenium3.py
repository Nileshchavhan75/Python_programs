from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://www.google.com")
time.sleep(2)

# Step 3: Find the textbox (Search input field)
search_box = driver.find_element(By.NAME, "q")

# Step 4: Type text into the textbox using send_keys()
search_box.send_keys("Selenium WebDriver in Python")
time.sleep(2)

# Step 5: Press ENTER key to click the "Google Search" button
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Step 6: Print the title of the result page
print("Page Title:", driver.title)

# Step 7: Close the browser
time.sleep(5)
driver.quit()
