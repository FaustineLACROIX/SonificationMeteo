import requests

WEATHER_CODES = {
    0: "Ensoleilé",
    1: "Ensoleilé",
    2: "Nuageux",  # Fusion de "Partiellement nuageux" et "Couvert"
    3: "Nuageux",
    45: "Brumeux",  # Fusion de Brouillard et Brouillard givrant
    48: "Brumeux",
    51: "Pluvieux",
    53: "Pluvieux",
    55: "Pluvieux",
    61: "Pluvieux",  # Fusion avec averses légères
    63: "Pluvieux",  # Fusion avec averses modérées
    65: "Pluvieux",  # Fusion avec averses fortes
    80: "Pluvieux",
    81: "Pluvieux",
    82: "Pluvieux",
    71: "Neigeux",  
    73: "Neigeux",
    75: "Neigeux",
    77: "Neigeux",
    95: "Orageux",
    96: "Orageux"
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
    url = f"https://api.open-meteo.com/v1/forecast?latitude={x}&longitude={y}&minutely_15=temperature_2m,weather_code,precipitation,wind_speed_10m,direct_radiation,visibility&forecast_days=1"
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

def get_radiation(jsonObject):
    """
    return a list with 4 direct radiation values per hour for a all day
    """
    return jsonObject.get("minutely_15", {}).get("direct_radiation", [])

def get_visibility(jsonObject):
    """
    return a list with 4 visibilities values per hour for a all day
    """
    return jsonObject.get("minutely_15", {}).get("visibility", [])

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
# radiation = get_radiation(json)
# print(radiation)
# visibility = get_visibility(json)
# print(visibility)

# # print("Température :",temp , "°C")
# print("Météo :", weather[30])
# print("Vitesse du vent :", wind[30], "km/h")
# print("Précipitations :", rain[30], "mm")
# print("Radiation :", radiation[30], "W/m^2")
# print("Visibility :", visibility[30], "m" )
