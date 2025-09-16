from fastapi import FastAPI, Query
from data_processing import MYH

app = FastAPI()


@app.get("/myh/")
def read_myh_data(limit: int = Query(100, gt=0), school: str = Query(None)):
    myh = MYH(limit)

    # TODO: filter out the school
    # you probably need to add a method in MYH class in data_processing as well



    return myh.to_json()
