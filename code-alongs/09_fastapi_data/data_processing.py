import pandas as pd 
from constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "Sales.csv")


class DataExplorer:
    def __init__(self, limit = 100):
        self._df = df.head(limit)


if __name__ == "__main__":
    data_explorer = DataExplorer()

    print(data_explorer._df)