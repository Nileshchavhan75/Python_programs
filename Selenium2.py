from selenium import webdriver
import time

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()

# 1. Open a website
driver.get("https://www.google.com")

# 2. Maximize the window
driver.maximize_window()
time.sleep(2)

# 3. Refresh the page
driver.refresh()
time.sleep(2)

# 4. Get the page title
print("Page Title:", driver.title)

# 5. Get the current URL
print("Current URL:", driver.current_url)

# 6. Navigate to another page
driver.get("https://www.bing.com")
time.sleep(2)

# 7. Go back to the previous page
driver.back()
time.sleep(2)

# 8. Go forward to the next page
driver.forward()
time.sleep(2)

# 9. Minimize the window
driver.minimize_window()
time.sleep(2)

# 10. Keep browser open until user presses Enter
input("Press Enter to close the browser...")

# Close browser
driver.quit()
