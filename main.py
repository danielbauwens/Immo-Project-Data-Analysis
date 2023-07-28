from preprocessing import cleanup
from predict import model_linear
import pandas as pd
import numpy as np
from fastapi import FastAPI, Body

app = FastAPI()

# Returns the predicted house value when requested with the correct information.
@app.post("/predict/")
def prediction(predict: dict = Body()):
    # Both the dataset and prediction values are pre-processed together (if necessary).
    df = pd.read_csv('../data/merged_data.csv')
    df = cleanup(df, predict)
    dfpredict = df.tail(1)
    dfpredict = dfpredict.drop('price', axis=1)
    df = df.drop(df.index[-1])
    predictx = model_linear(df, dfpredict)
    predictx = int(predictx)
    return f"The estimated price is: €{predictx}"

# Returns an example dictionary of the format required to get a prediction.
@app.get("/")
def predictmodel():
    predictx = {
    "Zip code": 0, 
    "subtype": "", 
    "bedrooms": 0, 
    "Living area": 0, 
    "landplot": 0, 
    "facades": 0, 
    "condition": "", 
    "province": ""
    }
    return f"Fill in this dictionary structure and send to endpoint '/predict/' to get a prediction: {predictx}"