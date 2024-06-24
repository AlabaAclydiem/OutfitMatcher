import json
import os
from datetime import datetime, timedelta

import requests


class WeatherCityInfo:
    def __init__(self, city="Minsk") -> None:
        self.city = city
        self.longitude = None
        self.latitude = None
        self._set_city_coordinates()

    def _set_city_coordinates(self):
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={self.city}&count=1&language=en&format=json"
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
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&wind_speed_unit=ms&timezone=auto"
        return self._get_json(requests.get(url))

    def get_today_forecast(self) -> None:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,cloud_cover,wind_speed_10m&wind_speed_unit=ms&timezone=auto&forecast_days=1"
        return self._get_json(requests.get(url))

    def get_day_forecast(self, day: str) -> None:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,cloud_cover,wind_speed_10m&wind_speed_unit=ms&timezone=auto&start_date={day}&end_date={day}"
        return self._get_json(requests.get(url))
