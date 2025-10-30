# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# Words=[]
# Authorname=[]

# driver=webdriver.Chrome()

# for page in range(1, 11):  
#     url = f"https://quotes.toscrape.com/page/{page}/"
#     driver.get(url)
#     print(f"Scraping page {page}...")
# time.sleep(2)
    
# # driver.get("https://quotes.toscrape.com")
# # print("Title is ...",driver.title)

# pera=driver.find_elements(By.CLASS_NAME,"quote")

# for index ,text in enumerate(pera):
#     texts=text.find_element(By.CLASS_NAME,"text").text
#     author=text.find_element(By.CLASS_NAME,"author").text
#     time.sleep(5)
#     Words.append(texts)
#     Authorname.append(author)
#     try:
#         next_button = driver.find_element(By.LINK_TEXT, "Next")
#         next_button.click()
#         time.sleep(5)
#     except:
#         break
# driver.quit()

# df=pd.DataFrame({
#     "Text":Words,
#     "Authors":Authorname
# })

# df.to_excel("data.xlsx",index=False)
# print("Data Saved in Xcel SucessFully...")


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
Words = []
Authorname = []
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage") 
driver = webdriver.Chrome(options=chrome_options)
base_url = "https://quotes.toscrape.com"
driver.get(base_url)
while True:
    try:
        print(f"Scraping page {len(Words) // 10 + 1}...")
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            Words.append(text)
            Authorname.append(author)
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
        next_button.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Last page reached. Scraping completed.")
        break
    except ElementNotInteractableException as e:
        print(f"Error clicking 'Next' button: {e}")
        print("Attempting to break the loop as the button may not be clickable anymore.")
        break
driver.quit()
df = pd.DataFrame({
    "Text": Words,
    "Authors": Authorname
})

df.to_excel("data.xlsx", index=False)
print("Data Saved in Excel Successfully...")
print(f"Total quotes scraped: {len(Words)}")


