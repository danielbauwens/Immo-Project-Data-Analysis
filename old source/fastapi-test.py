from fastapi import FastAPI, Body
from pydantic import Basemodel

app = FastAPI()


@app.get("/salary/")
def salary(payload: dict = Body()):
    result = payload['salary']+payload['bonus']-payload['taxes']


    return f"Total Salary is {result} Euros."

    