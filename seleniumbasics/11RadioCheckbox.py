import time

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome( )
driver.get("https://demo.automationtesting.in/Register.html")

#Radio Button
driver.find_element(By.XPATH, "//input[@value='Male']").click()

#Check Box and get Attribute
li = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Movies':
        ele.click()

li1 = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for ele1 in li1:
    val1=ele1.get_attribute('value')
    print(val1)
    if val1 =='Movies':
        ele1.click()
        time.sleep(5)

li2=driver.find_elements(By.XPATH,"//input[@value='Male']")


for ele2 in li2:
    val3=ele2.get_attribute('value')
    print(val3)
    if val3 == 'Male':
        ele2.click()
        time.sleep(2)

