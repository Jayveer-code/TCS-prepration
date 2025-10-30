from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://jayveerportfolio.netlify.app/")
lorem=driver.find_element(By.CSS_SELECTOR,'p[data-sr-id="13"]').text
print("Lorem Text is ",lorem)
time.sleep(3)
driver.close()
