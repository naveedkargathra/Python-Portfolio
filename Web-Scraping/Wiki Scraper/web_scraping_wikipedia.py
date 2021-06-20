from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"

page_content = requests.get(url)
html_data = page_content.text
x = html_data[101:124]
print(x)

soup= BeautifulSoup(html_data, 'html.parser')
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in (soup.find_all('tbody')[3].find_all('tr')[1:]):
    col =row.find_all('td')
    
    name = col[1].text.strip()
    m_cap = col[2].text.strip()
    data= data.append({"Name":name, "Market Cap (US$ Billion)":m_cap}, ignore_index= True) 

  
print(data.head())

data.to_json('bank_market_cap.json')

