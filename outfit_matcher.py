from datetime import datetime

from clothes_memory import ClothesMemory
from outfit_model import OutfitModel
from weather_city_info import WeatherCityInfo


class OutfitMatcher:
    def __init__(self):
        self.dataset = ClothesMemory()
        self.model = OutfitModel()
        self.weather_api = WeatherCityInfo()

    def start(self):
        while True:
            command = input("Enter a command (now, today, YYYY-MM-DD, exit):\n")
            if command == "exit":
                print("Exiting...")
                break
            elif command == "now":
                prediction = self.model.predict(
                    prompt="Help me to choose proper clothes by color comfortouble for current weather",
                    clothes=matcher.dataset.to_json(),
                    outfit=matcher.dataset.previous_outfit,
                    weather=matcher.weather_api.get_current_weather(),
                )
                print(prediction)
            elif command == "today":
                prediction = self.model.predict(
                    prompt="Help me to choose proper clothes by color comfortouble for current weather",
                    clothes=matcher.dataset.to_json(),
                    outfit=matcher.dataset.previous_outfit,
                    weather=matcher.weather_api.get_today_forecast(),
                )
                print(prediction)
            else:
                try:
                    datetime.strptime(command, "%Y-%m-%d")
                    prediction = self.model.predict(
                        prompt="Help me to choose proper clothes by color comfortouble for current weather",
                        clothes=matcher.dataset.to_json(),
                        outfit=matcher.dataset.previous_outfit,
                        weather=matcher.weather_api.get_day_forecast(command),
                    )
                    print(prediction)
                except ValueError:
                    print("Wrong command")


if __name__ == "__main__":
    matcher = OutfitMatcher()
    matcher.start()
