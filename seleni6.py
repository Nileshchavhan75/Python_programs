from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()

try:
    driver.get("https://globbertrot.github.io/images/")
    image = driver.find_element(By.TAG_NAME, "img")
    print("Image Source:", image.get_attribute("src"))

except NoSuchElementException:
    print("No image found on the page.")
finally:
    time.sleep(10)
    driver.quit()