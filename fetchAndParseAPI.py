import requests

def convert_city_to_coordinate(city):
    pass


def fetch(coordinate):
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&minutely_15=temperature_2m"
    response = requests.get(url)
    return response.json()

def get_temperature():
    pass

def get_wind_speed():
    pass

def get_rainfall():
    pass

def get_weather_conditions():
    pass
