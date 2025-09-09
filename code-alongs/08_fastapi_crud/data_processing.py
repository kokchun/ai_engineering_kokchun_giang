from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field


def read_json(filename: str):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    return data


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(gt = 1500, lt = 2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 11,
                "title": "Learn with AIgineer",
                "author": "Kokchun Giang",
                "year": 2025,
            }
        }
    }


class Library(BaseModel):
    name: str
    books: list[Book]


def library_data(filename):
    """Deserializes library json data into a Library model"""
    json_data = read_json(filename)
    return Library.model_validate(json_data)


if __name__ == "__main__":

    data = library_data("library.json")

    pprint(data)
