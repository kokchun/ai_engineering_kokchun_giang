import pandas as pd 
from constants import DATA_PATH
from pydantic import BaseModel, Field

df = pd.read_csv(DATA_PATH / "Iris.csv", index_col=0)


class IrisData:
    def __init__(self):
        self.df = df

    def to_json(self):
        return self.df.to_dict(orient="records")
    
# request/response schemas
class IrisInput(BaseModel):
    SepalLengthCm: float = Field()
    SepalWidthCm: float = Field()
    PetalLengthCm: float = Field()
    PetalWidthCm: float = Field()

class PredictionOutput(BaseModel):
    predicted_flower: str



if __name__ == "__main__":
    iris = IrisData()
    print(iris.to_json())