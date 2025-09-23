from fastapi import FastAPI
from data_processing import IrisData, IrisInput, PredictionOutput
import pandas as pd 

app = FastAPI()

iris = IrisData()

@app.get("/api/")
def read_data():
    return iris.to_json()

@app.post("/api/predict", response_model=PredictionOutput)
def predict_flower(payload: IrisInput):
    data_to_predict = pd.DataFrame(payload.model_dump())