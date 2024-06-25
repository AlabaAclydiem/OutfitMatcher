import pandas as pd


class ClothesMemory:
    def __init__(self, csv_path="./clothes.csv"):
        self.clothes = pd.read_csv(csv_path, sep=",")
        self.previous_outfit = None

    def to_json(self):
        return self.clothes.to_json(orient="records")

    def remember_outfit(self, outfit):
        self.previous_outfit = outfit
