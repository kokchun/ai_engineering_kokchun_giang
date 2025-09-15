from fastapi import FastAPI, APIRouter
from data_processing import DataExplorer


app = FastAPI()

router = APIRouter(prefix="/api/sales")


@router.get("")
async def read_sales():
    # implement this code to return json data in this endpoint

    data_explorer = DataExplorer()
    return data_explorer.json_response()


@router.get("/summary")
async def read_summary_data():
    """shows summary statistics"""
    data_explorer = DataExplorer()
    return data_explorer.summary().json_response()


@router.get("/kpis")
async def read_kpis_by_country(country: str):
    """KPIs based on country"""
    data_explorer = DataExplorer()
    return data_explorer.kpis(country=country)


app.include_router(router)

# to run the API
# uvicorn api:app --reload

# navigate to /docs for swagger ui
