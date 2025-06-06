from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # for CI/CD servers

driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com")

driver.find_element(By.ID, "email").send_keys("testuser@example.com")
driver.find_element(By.ID, "pass").send_keys("yourpassword")
driver.find_element(By.ID, "loginbutton").click()

time.sleep(5)
driver.quit()
