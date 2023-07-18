from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def model():
    # Defining 'X' and 'y' variables from our dataframe using purely features that contain numerical data.
    X = df.drop(['price'], axis=1).to_numpy()
    y = df['price'].to_numpy()