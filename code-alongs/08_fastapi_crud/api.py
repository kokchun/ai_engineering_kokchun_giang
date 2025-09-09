from fastapi import FastAPI
from data_processing import library_data

app = FastAPI()

library = library_data("library.json")
books = library.books


@app.get("/books")
async def read_books():
    return books