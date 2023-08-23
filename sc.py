from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Replace this with the URL of the website you want to interact with
url = "https://example.com"

# Replace this with the text you want to find and click on
text_to_find = "Your Text Here"
dropdown_option = "Option to Select"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the specified URL
driver.get(url)

# Wait for the page to load (you can adjust the time as needed)
time.sleep(3)

try:
    # Find the input element containing the specified text
    input_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")
    
    # Scroll to the element to make sure it's in view
    driver.execute_script("arguments[0].scrollIntoView();", input_element)
    
    # Click on the element
    input_element.click()

    # Wait for a moment to allow any interactions to take effect
    time.sleep(2)
    
    # Find and select an option from the dropdown
    dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
    dropdown.select_by_visible_text(dropdown_option)
    
    # Find and click the "Add" button
    add_button = driver.find_element(By.ID, "add_button_id")
    add_button.click()
    
    # Wait for a moment to allow the changes to take effect
    time.sleep(2)
    
    # Find and enter text in the input field
    text_input = driver.find_element(By.ID, "text_input_id")
    text_input.clear()
    text_input.send_keys("ABCD")
    
    # Find and click the "Apply" button
    apply_button = driver.find_element(By.ID, "apply_button_id")
    apply_button.click()
    
    # Wait for a moment to allow the changes to take effect
    time.sleep(2)
    
    # Find and click the "Refresh" button
    refresh_button = driver.find_element(By.ID, "refresh_button_id")
    refresh_button.click()

    # Wait for a moment to allow the changes to take effect
    time.sleep(2)

    # Take a screenshot of the screen
    driver.save_screenshot("screenshot.png")

finally:
    # Close the browser window
    driver.quit()
