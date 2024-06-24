import pandas as pd


class ClothesDataset:
    def __init__(self, csv_path="./clothes.csv"):
        self.clothes = pd.read_csv(csv_path, sep=",")

    def to_json(self):
        return self.clothes.to_json(orient="records")
