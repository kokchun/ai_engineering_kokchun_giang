from fastapi import FastAPI

app = FastAPI()

@app.get("/api/sales")
async def read_sales():
    # implement this code to return json data in this endpoint
    return ...

@app.get("/api/summary")
async def read_summary_data():
    """shows summary statistics"""
    return ...