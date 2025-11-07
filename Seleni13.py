from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/tool-tips")

btn = driver.find_element(By.ID, "toolTipButton")
ActionChains(driver).move_to_element(btn).perform()
time.sleep(2)

tooltip = driver.find_element(By.CLASS_NAME, "tooltip-inner")
print("Tooltip Text:", tooltip.text)

time.sleep(5)
driver.quit()
 