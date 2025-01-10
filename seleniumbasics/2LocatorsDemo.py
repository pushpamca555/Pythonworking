import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manages ChromeDriver

# Set up WebDriver
driver = webdriver.Chrome()
# Open a webpage
driver.get("https://www.google.com")
# Close the browser
driver.quit()
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")

'''Locators:
By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.CSS_SELECTOR
By.XPATH'''

email_text = driver.find_element(By.ID,'email')
email_text.send_keys("test@gmail.com")
time.sleep(2)
driver.find_element(By.ID,'enterimg').click()