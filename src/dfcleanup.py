import pandas as pd
import numpy as np

def cleaning(df):
    # Filling NaN values with 0.
    df['landplot'].fillna(0, inplace=True)
    df['facades'].fillna(0, inplace=True)
    df['Living area'].fillna(0, inplace=True)

    # Creating dummy columns from categorical data.
    df = pd.get_dummies(df, columns=['condition', 'subtype', 'province', 'Zip code'])

    # Removing features that we won't be using.
    df.drop(['type', 'city', 'facades', 'Terrace', 'Kitchen'], axis=1, inplace=True)

    # Because 'get_dummies()' creates boolean values, we re-define our dataframe to be integers only.
    df = df.astype(int)
