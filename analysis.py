#import seaborn as sns
import pandas as pd
from bs4 import BeautifulSoup
import requests

#ds = pd.read_csv('main_property_data.csv')
data = requests.get('https://www.metatopos.eu/belgcombiN.html')
soup = BeautifulSoup(data.content, 'html.parser')
zipcodes =[]
cities =[]
subcities =[]
provinces =[]
conscern = soup.find_all("td")
for i in range(0, len(conscern), 7):
    zipcodes.append(conscern[i].text)
    cities.append(conscern[i+1].text)
    subcities.append(conscern[i+2].text)
    provinces.append(conscern[i+3].text)

df = pd.DataFrame({'Zip code': zipcodes, 'city': cities, 'subcity': subcities, 'province': provinces})
#df.to_csv('zipcodes.csv', index=False)
df.drop(df['subcity'], inplace=True, axis=1)
df.drop_duplicates('first', inplace=True)
ds1 = pd.read_csv('main_property_data.csv')
ds1=  ds1.sort_values('Zip code', inplace=True)
ds2 = df.sort_values('Zip code', inplace=True)
ds1['Zip code'] = ds1['Zip code'].astype(str)
merged = pd.merge(ds1, ds2, on='Zip code')
merged.to_csv('merged_data.csv', index=False)