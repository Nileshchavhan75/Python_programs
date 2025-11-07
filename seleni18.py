from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os

# ✅ Create a separate Chrome profile folder for Selenium
selenium_profile_path = os.path.join(os.getcwd(), "selenium_chrome_profile")

options = Options()
options.add_argument(f"user-data-dir={selenium_profile_path}")
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")

# Launch Chrome with new profile
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.python.org")

print("✅ Chrome launched successfully with a new profile!")
print("Page title:", driver.title)

driver.quit()
