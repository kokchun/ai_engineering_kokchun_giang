from fastapi import FastAPI
from utils import query_duckdb
from agents import movie_agent
from data_models import Prompt

app = FastAPI()

@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;")
    return movies.to_dict(orient="records")


@app.post("/create_movie")
async def create_movie(query: Prompt):
    result = await movie_agent.run(query.prompt)
    
    # db logic to save movie


    return result.output
