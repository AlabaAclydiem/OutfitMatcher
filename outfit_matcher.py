from clothes_dataset import ClothesDataset
from outfit_model import OutfitModel
from weather_city_info import WeatherCityInfo


class OutfitMatcher:
    def __init__(self):
        self.dataset = ClothesDataset()
        self.model = OutfitModel()
        self.weather_api = WeatherCityInfo()

    def start(self):
        while True:
            pass


matcher = OutfitMatcher()
print(
    matcher.model.predict(
        prompt="Help me to choose proper clothes by color and weather",
        clothes=matcher.dataset.to_json(),
        weather=matcher.weather_api.get_day_forecast("2024-06-25"),
    )
)
