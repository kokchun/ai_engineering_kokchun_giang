from constants import DATA_PATH
import pandas as pd
import json


df = pd.read_excel(
    DATA_PATH / "resultat-ansokningsomgang-2024.xlsx", sheet_name="Tabell 3", header=5
)


class MYH:
    def __init__(self, limit: int = 100):
        self.df_full = df
        self.df = df.head(limit)

    def filter_school(self, school: str):
        self.df = self.df_full.query(
            "`Utbildningsanordnare administrativ enhet` == @school"
        )

        return self

    def to_json(self):
        data = self.df.to_json(orient="records")
        return json.loads(data)
