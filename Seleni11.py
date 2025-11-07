from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(2)

# Locate the table
table = driver.find_element(By.ID, "customers")

# Get all rows
rows = table.find_elements(By.TAG_NAME, "tr")

# Iterate through rows and print each cell value
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text, end=" | ")
    print()

time.sleep(5)
driver.quit()
