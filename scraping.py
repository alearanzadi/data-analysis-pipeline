import pandas as pd
import requests as req
from clean import data_last

url = "https://countrycode.org"
res = req.get(url)
res.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

lst_elements = soup.select("tr td a")
countries =[]

for e in lst_elements:
    countries.append(e.text)
    
countries=countries[:240]

lst_gdp = soup.select("tr td")

gdp = list(map(lambda x : x.text,lst_gdp))[5::6][:240]

df = pd.DataFrame()
df["countries"]=countries
df["gdp"]=gdp

lst2 = []

for i in df['gdp']:
    lst2.append(i.split(" "))


numeros=[]
for e in lst2:
    if len(e)==1: 
        numeros.append(0)
        
    else: 
        num=float(e[0])
        if len(e)==2:
            if 'M' in e[1]: num*=10e5
            elif 'B' in e[1]: num*=10e8
            elif 'T' in e[1]: num*=10e11
            numeros.append(num)

df["gdp"]=numeros
df_cero = df[(df["gdp"]==0)]

data_final = df[df["gdp"]!=0]
data_final.sort_values(by='gdp',ascending=False)

data_merge = data_final.merge(data_last, on='Country Name', how='inner')
data_merge.sort_values('gdp', ascending=False)

data_merge.describe()