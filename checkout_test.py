from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open SauceDemo site
driver.get("https://www.saucedemo.com")

# Step 3: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Step 4: Add a product to cart
driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

# Step 5: Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# Step 6: Click Checkout
driver.find_element(By.ID, "checkout").click()

# Step 7: Enter user info
driver.find_element(By.ID, "first-name").send_keys("Shivam")
driver.find_element(By.ID, "last-name").send_keys("Jaswal")
driver.find_element(By.ID, "postal-code").send_keys("174021")

# Step 8: Click Continue
driver.find_element(By.ID, "continue").click()

# Step 9: Click Finish
driver.find_element(By.ID, "finish").click()
time.sleep(1)

# Step 10: Confirm success
confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text
if "THANK YOU FOR YOUR ORDER" in confirmation.upper():
    print("✅ Checkout completed successfully.")
else:
    print("❌ Checkout failed.")

# Step 11: Close browser
driver.quit()
