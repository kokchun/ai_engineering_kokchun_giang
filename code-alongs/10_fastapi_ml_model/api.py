from fastapi import FastAPI
from data_processing import IrisData

app = FastAPI()

iris = IrisData()

@app.get("/api/")
def read_data():
    return iris.to_json()