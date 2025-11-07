from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

actions = ActionChains(driver)

# Right Click and handle alert
actions.context_click(driver.find_element(By.XPATH, "//span[text()='right click me']")).perform()
driver.find_element(By.XPATH, "//span[text()='Edit']").click()
print("Right click -> Edit clicked.")
time.sleep(1)
driver.switch_to.alert.accept()

# Double Click and handle alert
actions.double_click(driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")).perform()
print("Double click performed.")
time.sleep(1)
driver.switch_to.alert.accept()

driver.quit()
