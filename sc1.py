from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace this with the URL of the website you want to interact with
url = "https://example.com"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the specified URL
driver.get(url)

# Wait for the page to load (you can adjust the time as needed)
time.sleep(3)

try:
    # Locate the refresh button and click it
    refresh_button = driver.find_element(By.ID, "refresh_button_id")
    refresh_button.click()

    # Wait for the page to refresh
    time.sleep(3)

    # Find all the rows in the table
    table_rows = driver.find_elements(By.XPATH, "//table//tbody/tr")

    # Assuming the desired filter option is in the third cell of the first row
    filter_cell = table_rows[0].find_elements(By.TAG_NAME, "td")[2]

    # Find the filter option within the cell and click it
    filter_option = filter_cell.find_element(By.XPATH, ".//button[contains(text(), 'Filter Option')]")
    filter_option.click()

    # Wait for a moment for the filter options to appear
    time.sleep(2)

finally:
    # Close the browser window
    driver.quit()
