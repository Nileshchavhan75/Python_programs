from selenium import webdriver
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open a web page
driver.get("https://www.google.com")
driver.maximize_window()
print("Opened Google Homepage")

# ----- Window Size -----
print("\n--- Window Size ---")
print("Current Size:", driver.get_window_size())

# Change window size
driver.set_window_size(800, 600)
print("New Size:", driver.get_window_size())

# ----- Window Position -----
print("\n--- Window Position ---")
print("Current Position:", driver.get_window_position())

# Change window position
driver.set_window_position(100, 100)
print("New Position:", driver.get_window_position())

# ----- Open a New Window -----
print("\n--- Multiple Window Handling ---")
driver.execute_script("window.open('https://www.python.org', '_blank');")
time.sleep(5)

# Get all window handles
all_windows = driver.window_handles
print("All Windows:", all_windows)

# Switch to the new window
driver.switch_to.window(all_windows[1])
print("Switched to New Window Title:", driver.title)
time.sleep(5)

# Close the new window
driver.close()
print("Closed the new window")

# Switch back to the main window
driver.switch_to.window(all_windows[0])
print("Back to Main Window Title:", driver.title)

# Quit the browser
driver.quit()
print("\n✅ Window handling demo completed successfully!")
