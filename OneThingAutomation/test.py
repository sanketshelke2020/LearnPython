from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

div = driver.find_element(By.ID,'SIvCob')

elements = driver.find_elements(By.TAG_NAME, 'a')
for e in elements:
    print(e.text)
