# from selenium import webdriver
# import time
# dri = webdriver.Chrome()

# dri.get("https://www.google.com/")

# script="alert('Crome open successfully')"
# dri.execute_async_script(script)
# time.sleep(10)
# from selenium import webdriver
# import time 
# dri = webdriver.Chrome()

# dri.get("https://www.google.com")
# script="alert('Crome open successfully')"
# dri.execute_async_script(script)
# time.sleep(10)

from selenium import webdriver
import time

dri = webdriver.Chrome()

dri.get("https://www.google.com")
script = "alert('chrome open succssfully')"
dri.execute_async_script(script)
time.sleep(10)