from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel

def read_json(filename: str):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    return data


class Book(BaseModel):
    id: int 
    title: str 
    author: str 
    year: int

class Library(BaseModel):
    name: str 
    books: list[Book]

if __name__ == '__main__':

    data = read_json("library.json")

    pprint(data)

