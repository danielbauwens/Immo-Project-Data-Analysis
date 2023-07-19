import pandas as pd
import numpy as np

def cleaning(df):
    '''Holds the code to clean and pre-process our scraped data before training our ML model on it.'''

    # Filling NaN values with 0.
    df['landplot'].fillna(0, inplace=True)
    df['facades'].fillna(0, inplace=True)
    df['Living area'].fillna(0, inplace=True)

    # Reduces zip codes to 2 digits for broader scope.
    df['Zip code'] = (df['Zip code']/100).astype(int)

    # Creating dummy columns from categorical data.
    df = pd.get_dummies(df, columns=['condition', 'province', 'Zip code', 'subtype'])

    # Removing features that we won't be using.
    df.drop(['city', 'Kitchen', 'Terrace', 'type'], axis=1, inplace=True)

    # Because 'get_dummies()' creates boolean values, we re-define our dataframe to be integers only.
    df = df.astype(int)
    return df