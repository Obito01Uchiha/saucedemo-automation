from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome WebDriver (chromedriver.exe is in same folder)
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com")

# Enter login credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login
driver.find_element(By.ID, "login-button").click()

# Wait for page to load
time.sleep(2)

# Check if login successful
if "inventory" in driver.current_url:
    print("✅ Login successful")
else:
    print("❌ Login failed")

# Close browser
driver.quit()
