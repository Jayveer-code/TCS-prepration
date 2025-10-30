from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.get("https://www.w3schools.com/html/html_tables.asp")
table=d.find_element(By.ID,"customers")
rows=table.find_elements(By.TAG_NAME,"tr")
for row in rows[1:]:
    cells=row.find_elements(By.TAG_NAME,"td")
    if cells:
        print(f"compnay :{cells[0].text} ,contact is ,{cells[1].text},country is {cells[2].text}")
d.quit()
        
