# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Register.html")
#
# # Xpath
# # Syntax
# # //tagname[@attribute='value'] or //*[@attribute='value']
# # //input[@placeholder='First Name']
# # //*[@placeholder='First Name']
# # text
# //label[text()='Full Name* ']
#
# # contains
# //label[contains(text(),'Full Name')]
#
# # index
# //label[2]
#
# # OR & AND
# //*[@placeholder='First Name' and @ng-model="FirstName"]
# //*[@placeholder='First Name' or @ng-model="FirstName"]
#
# # parent - Child - ancestor
# //form[@id='basicBootstrapForm']/child::div
# //form[@id='basicBootstrapForm']/parent::div
# //grandparents - up of mine
# //form[@id='basicBootstrapForm']/ancestor::div
#
#
# # following- sibling - preceding
# //input[@id='checkbox1']//following-sibling::label
# //input[@id='checkbox1']//preceding-sibling::label
