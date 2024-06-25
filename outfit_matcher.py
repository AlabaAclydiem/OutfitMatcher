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
            outfit=matcher.dataset.previous_outfit,
            weather=weather_func(*args),
        )

    def start(self):
        while True:
            command = input("Enter a command (now, today, YYYY-MM-DD, exit):\n")
            if command == "exit":
                print("Exiting...")
                break
            elif command == "now":
                print(self.match(self.weather_api.get_current_weather))
            elif command == "today":
                print(self.match(self.weather_api.get_today_forecast))
            else:
                try:
                    datetime.strptime(command, "%Y-%m-%d")
                    print(self.match(self.weather_api.get_day_forecast, command))
                except ValueError:
                    print("Wrong command")


if __name__ == "__main__":
    matcher = OutfitMatcher()
    matcher.start()
