import pandas as pd
import numpy as np

def cleaning(df):

    df['landplot'].fillna(0, inplace=True)
    df['facades'].fillna(0, inplace=True)
    df['Living area'].fillna(0, inplace=True)