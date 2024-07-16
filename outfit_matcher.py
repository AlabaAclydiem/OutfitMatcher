from datetime import datetime

from clothes_memory import ClothesMemory
from outfit_model import OutfitModel
from weather_city_info import WeatherCityInfo


class OutfitMatcher:
    def __init__(self):
        self.dataset = ClothesMemory()
        self.model = OutfitModel()
        self.weather_api = WeatherCityInfo()

    def match(self, include_hours, weather_func, args=None):
        return self.model.predict(
            clothes=matcher.dataset.to_json(),
            outfit=matcher.dataset.get_outfit(),
            weather=weather_func(*args),  
                  
        )

    def start(self):
        while True:
            command = input("Enter a command (now, today, YYYY-MM-DD, exit) or setting option (city, hours):\n")
            match command:
                case "city":
                    city = input('Enter a city name:\n')
                    try:
                        self.weather_api.set_city(city)
                    except ValueError as e:
                        print(e)
                case "hours":
                    hours = tuple(mao(int, input("Enter two numbers between 0 and 23 separated by space").split()))
                    
                case "exit":
                    print("Exiting...")
                    break
                case "now":
                    outfit = self.match(include_hours=False, weather_func=self.weather_api.get_current_weather)
                    print(outfit)
                    self.dataset.save_outfit(self.model.extract_outfit(outfit))
                case "today":
                    outfit = self.match(include_hours=True, weather_func=self.weather_api.get_today_forecast)
                    print(outfit)
                    self.dataset.save_outfit(self.model.extract_outfit(outfit))
                case _:
                    try:
                        datetime.strptime(command, "%Y-%m-%d")
                        outfit = self.match(include_hours=False, weather_func=self.weather_api.get_day_forecast, args=[command])
                        print(outfit)
                        self.dataset.save_outfit(self.model.extract_outfit(outfit))
                    except ValueError:
                        print("Wrong command")


if __name__ == "__main__":
    matcher = OutfitMatcher()
    matcher.start()
