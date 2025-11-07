from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Launch browser
driver = webdriver.Chrome()
driver.get("file:///C:/Python/wait_demo.html")   # Change path if needed
driver.maximize_window()

# 1️⃣ Implicit Wait
driver.implicitly_wait(5)
t1 = driver.find_element(By.ID, "text1")
print("Implicit Wait:", t1.text)

# 2️⃣ Explicit Wait
wait = WebDriverWait(driver, 10)
t2 = wait.until(EC.visibility_of_element_located((By.ID, "text2")))
print("Explicit Wait:", t2.text)

# 3️⃣ Fluent Wait
fluent = WebDriverWait(driver, 15, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
t3 = fluent.until(EC.visibility_of_element_located((By.ID, "text3")))
print("Fluent Wait:", t3.text)

driver.quit()
print("✅ Done! All waits worked successfully.")
