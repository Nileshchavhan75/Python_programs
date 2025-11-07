from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

driver.maximize_window()
print("maximize window")
time.sleep(2)

driver.minimize_window()
print("minimize window")
time.sleep(2)

driver.set_window_size(800,600)
print("set window size")
time.sleep(2)

driver.set_window_position(100,50)
print("window move to (100,50)")
time.sleep(2)

time.sleep(10)

driver.quit()