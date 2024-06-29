import pandas as pd


class ClothesMemory:
    def __init__(self, csv_path="./clothes.csv", outfit_path="./outfit.txt"):
        self.clothes = pd.read_csv(csv_path, sep=",")
        self.outfit_path = outfit_path
        self.previous_outfit = None

    def to_json(self):
        return self.clothes.to_json(orient="records")

    def save_outfit(self, outfit):
        self.previous_outfit = outfit
        with open(self.outfit_path, "w") as file:
            file.write(outfit)

    def get_outfit(self):
        if self.previous_outfit is None:
            try:
                with open(self.outfit_path, "r") as file:
                    self.previous_outfit = file.read()
            except FileNotFoundError:
                pass
        return self.previous_outfit
