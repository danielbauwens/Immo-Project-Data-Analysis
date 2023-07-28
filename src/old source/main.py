from dfcleanup import cleaning
from training_linear import model_linear
from training_decision_tree import model_tree
from training_boost import model_boost
from training_forest import model_forest
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Insert your CSV file in 'dataframe' variable, and call the 'cleaning()' function to process it before training our model.
dataframe = pd.read_csv('./data/merged_data.csv')
df = cleaning(dataframe)

# Instantiating our different Regressors.
reg = LinearRegression()
dtr = DecisionTreeRegressor()
xg = XGBRegressor()
rforest = RandomForestRegressor()

# Defining 'X' and 'y' variables from our dataframe using purely features that contain numerical data.
X = df.drop(['price'], axis=1).to_numpy()
y = df['price'].to_numpy()

# Reshaping 'y' to be 2D array. Optional. To get score from RandomForest, needs to be commented out.
#y = y.reshape(-1, 1) 

# Setting up 'train_test_split' to get standardized training/testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # Random state can be added to get the same results every time.


# Calling our training/testing models with our dataframe and the corresponding regression functions.
model_linear(df, reg, X_train, X_test, y_train, y_test) # LinearRegression()
model_tree(df, dtr, X_train, X_test, y_train, y_test) # DecisionTree()
model_boost(df, xg, X_train, X_test, y_train, y_test) # XGBoost()
model_forest(df, rforest, X_train, X_test, y_train, y_test) # RandomForest()