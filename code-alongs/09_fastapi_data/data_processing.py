import pandas as pd 
from constants import DATA_PATH
from pprint import pprint

df = pd.read_csv(DATA_PATH / "Sales.csv")


class DataExplorer:
    def __init__(self, limit = 100):
        self._df = df.head(limit)

    @property
    def df(self):
        return self._df
    

    def json_response(self):
        json_data = self.df.to_json(orient = "records")
        return json_data

if __name__ == "__main__":
    data_explorer = DataExplorer()

    pprint(data_explorer.json_response())