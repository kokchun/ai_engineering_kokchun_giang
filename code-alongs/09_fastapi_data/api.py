from fastapi import FastAPI
from data_processing import DataExplorer

data_explorer = DataExplorer()

app = FastAPI()

@app.get("/api/sales")
async def read_sales():
    # implement this code to return json data in this endpoint

    return data_explorer.json_response()

@app.get("/api/sales/summary")
async def read_summary_data():
    """shows summary statistics"""
    return data_explorer.summary().json_response()


@app.get("/api/sales/kpis")
async def read_kpis_by_country(country: str):
    """KPIs based on country"""
    return data_explorer.kpis(country=country)

# to run the API
# uvicorn api:app --reload

# navigate to /docs for swagger ui