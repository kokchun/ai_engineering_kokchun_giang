from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: int = Field(
        gt=0,
        lt=6,
        description="Rating of the movie between 1 and 5, the higher the better",
    )


class Prompt(BaseModel):
    prompt: str