from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Install and get the correct path for ChromeDriver
chromedriver_dir = ChromeDriverManager().install()
chromedriver_path = os.path.join(os.path.dirname(chromedriver_dir), 'chromedriver.exe')
print(f"Correct ChromeDriver path: {chromedriver_path}")

# Set up the webdriver with the correct executable path
web = webdriver.Chrome(service=ChromeService(chromedriver_path))

try:
    # Open Nike website
    web.get("https://www.nike.com/")
    print("Nike website opened.")
    web.maximize_window()
    time.sleep(2)

    # Wait until the search bar is visible and locate it
    wait = WebDriverWait(web, 20)
    search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='gn-search-input']")))
    print("Search bar located.")
    
    # Enter 'shoe' into the search bar and hit enter
    search_bar.send_keys("Air Force 1")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)
    print("Search term entered.")
    
    # Wait for search results to load
    results_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'product-grid')]")))
    print("Search results loaded.")
    time.sleep(2)
    
    # Click on the first search result link
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='skip-to-products']/div[1]/div/figure/a[2]/div/img")))
    first_result.click()
    print("First search result clicked.")
    time.sleep(2)

    # Select a shoe size (Example XPath; may need to be updated based on actual page layout)
    sizeclick = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='size-selector']/fieldset/div/div[8]/label")))
    sizeclick.click()
    print("Size is selected.")
    time.sleep(2)

    # Scroll and click on 'Add to Favorites'
    web.execute_script("window.scrollBy(0, 500);")
    fava = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div[2]/div[3]/div[5]/div[2]/button")))
    fava.click()
    print("Trying to add to Favorites.")
    time.sleep(2)
   
    # Enter email for sign-in
    emailenter = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='username']")))
    emailenter.send_keys("hariharanr2008@gmail.com")
    print("Email is entered for sign-in.")
    time.sleep(2)

    # Click the continue button
    continuee = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div/div/form/div/div[4]/button")))
    continuee.click()
    print("Clicking the continue button.")
    time.sleep(2)

finally:
    # Keeping the browser open for inspection
    print("Script completed. Browser will remain open for further inspection.")
    # Uncomment the following line to close the browser after inspection
    # web.quit()