from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.get("https://www.gridlastic.com/")
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, 'a')
for index, link in  enumerate(links):
    href=link.get_attribute('href')
    print(f'Links  no {index+1}  is {href}')

time.sleep(2)
driver.quit()
