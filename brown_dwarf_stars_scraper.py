from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bso
import time
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome(
    "C:/Users/HP/Downloads/chromedriver_win32 (1)/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []


page = requests.get(START_URL)

soup = bso(page.text,'html.parser')

star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)


temp_list= []


table_rows = star_table[2].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

headers = ['Star_name','Distance','Mass','Radius']
new_planet_df_1 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
new_planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")