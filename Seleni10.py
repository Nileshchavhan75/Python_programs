from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the button to trigger alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to alert and accept it
alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(2)
alert.accept()

# Keep browser open for 5 seconds
time.sleep(5)
driver.quit()
