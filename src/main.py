from src.dfcleanup import cleaning
from src.training import model
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Insert your CSV file in 'df' and call the 'cleaning()' function to process it before training our model.
df = cleaning(pd.read_csv('../data/merged_data.csv'))

# Instantiating LinearRegression as 'reg'.
reg = LinearRegression()

# Calling our training/testing model with our dataframe and 
model(df, reg)