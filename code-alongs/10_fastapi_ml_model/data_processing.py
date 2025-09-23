import pandas as pd 
from constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "Iris.csv", index_col=0)


class IrisData:
    def __init__(self):
        self.df = df

    def to_json(self):
        return self.df.to_dict(orient="records")
    
if __name__ == "__main__":
    iris = IrisData()
    print(iris.to_json())