from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open SauceDemo site
driver.get("https://www.saucedemo.com")

# Step 2: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Step 3: Add first product to cart
driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

# Step 4: Go to cart page
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(2)

# Step 5: Verify product is in cart
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
if len(cart_items) > 0:
    print("✅ Product added to cart successfully.")
else:
    print("❌ Cart is empty.")

# Close browser
driver.quit()
