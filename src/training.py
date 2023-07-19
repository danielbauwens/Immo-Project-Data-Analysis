from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def model(df, reg):
    '''Handles the code to train and test our cleaned dataset on.'''


    # Defining 'X' and 'y' variables from our dataframe using purely features that contain numerical data.
    X = df.drop(['price'], axis=1).to_numpy()
    y = df['price'].to_numpy()

    # Reshaping 'y' to be 2D array.
    y = y.reshape(-1, 1)

    # Setting up 'train_test_split' to get standardized training/testing sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # Random state can be added to get the same results every time.

    # Training our model.
    reg.fit(X_train, y_train)

    # Displaying score of Training variables.
    print("Training score:", reg.score(X_train, y_train)) 

    # Predicting the 'y' target value (Price).
    y_prediction = reg.predict(X_test)

    # Displaying the score of Testing variables
    features = X.shape[1]
    print("Testing score:", reg.score(X_test, y_test))
    print(f"Using {features} features, and 1 (price)target")