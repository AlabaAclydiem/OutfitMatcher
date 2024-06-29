from datetime import datetime

from clothes_memory import ClothesMemory
from outfit_model import OutfitModel
from weather_city_info import WeatherCityInfo


class OutfitMatcher:
    def __init__(self):
        self.dataset = ClothesMemory()
        self.model = OutfitModel()
        self.weather_api = WeatherCityInfo()

    def match(self, weather_func, *args):
        return self.model.predict(
            clothes=matcher.dataset.to_json(),
            outfit=matcher.dataset.get_outfit(),
            weather=weather_func(*args),
        )

    def start(self):
        while True:
            command = input("Enter a command (now, today, YYYY-MM-DD, exit):\n")
            if command == "exit":
                print("Exiting...")
                break
            elif command == "now":
                outfit = self.match(self.weather_api.get_current_weather)
                print(outfit)
                self.dataset.save_outfit(self.model.extract_outfit(outfit))
            elif command == "today":
                outfit = self.match(self.weather_api.get_today_forecast)
                print(outfit)
                self.dataset.save_outfit(self.model.extract_outfit(outfit))
            else:
                try:
                    datetime.strptime(command, "%Y-%m-%d")
                    outfit = self.match(self.weather_api.get_day_forecast, command)
                    print(outfit)
                    self.dataset.save_outfit(self.model.extract_outfit(outfit))
                except ValueError:
                    print("Wrong command")


if __name__ == "__main__":
    matcher = OutfitMatcher()
    matcher.start()
