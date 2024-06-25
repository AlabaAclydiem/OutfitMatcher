import requests

from weather_urls import (
    CITY_LATLONG_URL,
    WEATHER_CURRENT_URL,
    WEATHER_DAY_URL,
    WEATHER_TODAY_URL,
)


class WeatherCityInfo:
    def __init__(self, city="Minsk") -> None:
        self.city = city
        self.longitude = None
        self.latitude = None
        self._set_city_coordinates()

    def _set_city_coordinates(self):
        url = CITY_LATLONG_URL.format(self.city)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["results"][0]
            self.latitude = data["latitude"]
            self.longitude = data["longitude"]
        else:
            print("Error:", response.status_code, response.text)
            exit()

    def _get_json(self, response):
        if response.status_code == 200:
            return response.json()

    def set_city(self, city: str) -> None:
        self.city = city
        self._set_city_coordinates()

    def get_current_weather(self):
        url = WEATHER_CURRENT_URL.format(self.latitude, self.longitude)
        return self._get_json(requests.get(url))

    def get_today_forecast(self) -> None:
        url = WEATHER_TODAY_URL.format(self.latitude, self.longitude)
        return self._get_json(requests.get(url))

    def get_day_forecast(self, day: str) -> None:
        url = WEATHER_DAY_URL.format(self.latitude, self.longitude, day, day)
        return self._get_json(requests.get(url))
