import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')

if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

    
soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')


table_str = str(table)
df = pd.read_html((table_str))[0]

print(df)
