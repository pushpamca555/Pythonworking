from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # if path not added 1

#driver = webdriver.Chrome(service = Service(ChromeDriverManager().install())) # if path not added 2

# Set up WebDriver
driver = webdriver.Chrome()
# Open a webpage
driver.get("https://www.google.com")
driver.find_element(By.PARTIAL_LINK_TEXT,'How').click()
# Close the browser
driver.quit()
