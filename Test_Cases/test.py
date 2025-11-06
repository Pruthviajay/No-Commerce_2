from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

user_name=driver.find_element(By.ID,"Email")
user_name.clear()
user_name.send_keys("admin@yourstore.com")
time.sleep(2)