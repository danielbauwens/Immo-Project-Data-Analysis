#import seaborn as sns
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_city_info():
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
    df.to_csv('zipcodes.csv', index=False)

def cleanup():
    ds = pd.read_csv('./main_property_data.csv')
    df = pd.read_csv('./zipcodes.csv')

    ds.dropna(subset = ['Zip code'], inplace=True)
    ds.drop_duplicates(inplace=True)
    ds.rename(columns={'Type of property': 'type'}, inplace=True)
    ds.rename(columns={'Surface of the land(or plot of land)': 'landplot'}, inplace=True)
    ds.rename(columns={'Number of facades': 'facades'}, inplace=True)
    #ds.rename(columns={'Swimming pool': 'pool'}, inplace=True)
    ds.rename(columns={'State of the building': 'condition'}, inplace=True)
    ds.rename(columns={'Subtype of property': 'subtype'}, inplace=True)
    ds.rename(columns={'Price of property in euro': 'price'}, inplace=True)
    ds.rename(columns={'Number of bedrooms': 'bedrooms'}, inplace=True)
    ds.drop('ID number', inplace=True, axis=1)
    ds.drop('Raw num:', inplace=True, axis=1)
    ds.drop('Locality', inplace=True, axis=1)
    ds.drop('Garden', inplace=True, axis=1)
    ds.drop('Garden area', inplace=True, axis=1)
    ds.drop('Swimming pool', inplace=True, axis=1)
    #ds.drop('type', inplace=True, axis=1)
    #ds.drop('subtype', inplace=True, axis=1)
    ds.drop('Type of Sale', inplace=True, axis=1)
    ds.drop('URL', inplace=True, axis=1)
    #ds.drop('State of the building', inplace=True, axis=1)
    ds['Terrace'].fillna(0, inplace=True)
    #ds['Garden'].fillna(0, inplace=True)
    #ds['Garden area'].fillna(0, inplace=True)
    ds['Kitchen'].fillna(0, inplace=True)
    #ds['Type of Sale'].fillna('isUnknown', inplace=True)
    ds['Zip code'] = ds['Zip code'].astype(int)
    ds['Zip code'] = ds['Zip code'].astype(str)
    df.drop(index=df.index[0], axis=0, inplace=True)
    df.drop('subcity', inplace=True, axis=1)
    ds = ds.astype(str)
    df.drop_duplicates(subset=['Zip code'], keep='first', inplace=True)
    ds1 = ds.sort_values('Zip code')
    df = df.sort_values('Zip code')
    merged = pd.merge(ds1, df, on='Zip code', how='left', left_index=False)
    merged.to_csv('merged_data.csv', index=False)

cleanup()