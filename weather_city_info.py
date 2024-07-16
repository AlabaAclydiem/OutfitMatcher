import requests

from weather_urls import (
    CITY_LATLONG_URL,
    WEATHER_CURRENT_URL,
    WEATHER_DAY_URL,
    WEATHER_TODAY_URL,
)


class WeatherCityInfo:
    def __init__(self, city="Minsk", preffered_hours=(9, 20)) -> None:
        self.city = city
        self.longitude = None
        self.latitude = None
        self.preferred_hours = preffered_hours
        self._set_city_coordinates()
        self._check_hours()

    def _check_hours(self):
        if self.preferred_hours[0] > self.preferred_hours[1]:
            self.preferred_hours = (self.preferred_hours[1], self.preferred_hours[0])
        else:
            self.preferred_hours = (self.preferred_hours[0], self.preferred_hours[1])
        if self.preferred_hours[0] < 0 or self.preferred_hours[1] > 23:
            raise ValueError('Incorret day hours')
            
    def _set_city_coordinates(self):
        url = CITY_LATLONG_URL.format(self.city)
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()["results"][0]
            except KeyError:
                raise ValueError("Nonexisting city")
            self.latitude = data["latitude"]
            self.longitude = data["longitude"]
        else:
            print("Error:", response.status_code, response.text)
            exit()

    def _get_json(self, response):
        if response.status_code == 200:
            return response.json()

    def set_hours(self, preffered_hours: tuple[int, int]): 
        self.preferred_hours = preffered_hours
        self._check_hours()
    
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

