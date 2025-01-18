import pandas as pd
import requests
from bs4 import BeautifulSoup


url ="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')


table = soup.find('table',class_='wikitable')  #in this web page the data is stored in class wikitable as table

header = [th.text.strip() for th in table.find_all('th')]  #using list comprehension to get list of all headers

rows=[]           #empty list to store dara

for row in table.find_all('tr')[1:]:  #striping first row
    cols = row.find_all(['tr','td'])
    rows.append([col.text.strip() for col in cols])


df = pd.DataFrame(rows,columns = header)

print(df)
