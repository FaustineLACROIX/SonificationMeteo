import requests

WEATHER_CODES = {
    0: "Soleil",
    1: "Soleil",
    2: "Nuageux",  # Fusion de "Partiellement nuageux" et "Couvert"
    3: "Nuageux",
    45: "Brouillard",  # Fusion de Brouillard et Brouillard givrant
    48: "Brouillard",
    51: "Pluie",
    53: "Pluie",
    55: "Pluie",
    61: "Pluie",  # Fusion avec averses légères
    63: "Pluie",  # Fusion avec averses modérées
    65: "Pluie",  # Fusion avec averses fortes
    80: "Pluie",
    81: "Pluie",
    82: "Pluie",
    71: "Neige",  
    73: "Neige",
    75: "Neige",
    77: "Neige",
    95: "Orages",
    96: "Orages"
}


def convert_city_to_coordinate(city):
    url = f"https://api-adresse.data.gouv.fr/search/?q={city}"
    data = requests.get(url)
    parsed_data = data.json()
    return parsed_data["features"][0]["geometry"]["coordinates"]


def fetch(coordinate=[45, -0.5]):
    """
    return the jsonObject response for the api
    """
    x, y = coordinate 
    url = f"https://api.open-meteo.com/v1/forecast?latitude={x}&longitude={y}&minutely_15=temperature_2m,weather_code,precipitation,wind_speed_10m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_temperature(jsonObject):
    """
    return a list with 4 temperature values per hour for a all day   
    """ 
    return jsonObject.get("minutely_15", {}).get("temperature_2m", [])

def get_weather_conditions(jsonObject):
    """
    return a list with 4 conditions(sunny, cloudy, rainny, ....) values per hour for a all day
    """
    code = jsonObject.get("minutely_15", {}).get("weather_code", [])
    weather = []
    for i in range(len(code)):
        weather.append(WEATHER_CODES.get(code[i], "Code inconnu"))
    return weather

def get_wind_speed(jsonObject):
    """
    return a list with 4 wind speed values per hour for a all day
    """
    return jsonObject.get("minutely_15", {}).get("wind_speed_10m", [])

def get_rainfall(jsonObject):
    """
    return a list with 4 rainfall values per hour for a all day
    """
    return jsonObject.get("minutely_15", {}).get("precipitation", [])


#%% TEST---------------------------------------------------------
# coord = convert_city_to_coordinate("Bordeaux")
# print(coord)
# json = fetch(coord)
# print(json)

# temp = get_temperature(json)
# print(temp)
# weather = get_weather_conditions(json)
# print(weather)
# wind = get_wind_speed(json)
# print(wind)
# rain = get_rainfall(json)
# print(rain)

# print("Température :",temp , "°C")
# print("Météo :", weather)
# print("Vitesse du vent :", wind, "km/h")
# print("Précipitations :", rain, "mm")
