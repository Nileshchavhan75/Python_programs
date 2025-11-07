from selenium import webdriver
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.get("https://www.python.org")
driver.maximize_window()

# Scroll down and up by pixels
driver.execute_script("window.scrollBy(0, 500);")   # Scroll down
time.sleep(2)
driver.execute_script("window.scrollBy(0, -300);")  # Scroll up
time.sleep(2)

# Scroll to bottom and back to top
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")

# Keep browser open for observation
time.sleep(5)
driver.quit()
print("✅ Scrolling demo completed successfully!")
