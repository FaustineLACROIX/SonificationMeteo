from fetchAndParseAPI import *
from transformeWeatherToMusic import *
from generateMidi import *

city = "bordeaux"
coord = convert_city_to_coordinate(city)
first_note = 0
freq, list_instruments = default_settings()
personalize = "non"

json = {
  "latitude": 0.0,
  "longitude": 42.0,
  "generationtime_ms": 1.046895980834961,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 23.0,
  "minutely_15_units": {
    "time": "iso8601",
    "temperature_2m": "°C",
    "weather_code": "wmo code",
    "precipitation": "mm",
    "wind_speed_10m": "km/h",
    "direct_radiation": "W/m²",
    "visibility": "m"
  },
  "minutely_15": {
    "time": ["2025-04-07T00:00", "2025-04-07T00:15", "2025-04-07T00:30"],
    "temperature_2m": [-2.1, -2.0, -1.8, -2.1, -5.0, 1.8, 1, 2.0, 1.8, 2.1, -2.0, -4.8, -5.1, -7.0, -1.8],
    "weather_code": [75, 75, 75,75, 75, 75,75, 75, 75,75, 75, 75,75, 75, 75],
    "precipitation": [50.0, 50.1, 50.2, 50.0, 50.1, 20.2, 20.0, 10.1, 10.2, 10.0, 10.1, 30.2,30.0, 30.1, 40.2],
    "wind_speed_10m": [3.2, 3.4, 3.5,3.2, 3.4, 3.5,3.2, 3.4, 3.5,3.2, 3.4, 3.5,3.2, 3.4, 3.5],
    "direct_radiation": [20, 15, 10,20, 15, 10,20, 15, 10,20, 15, 10,20, 15, 10],
    "visibility": [5000, 4500, 4000,5000, 4500, 4000,5000, 4500, 4000,5000, 4500, 4000,5000, 4500, 4000]
  }
}

temp = get_temperature(json)
condi = get_weather_conditions(json)
wind = get_wind_speed(json)
rainfall = get_rainfall(json)
radiation = get_radiation(json)
visibility = get_visibility(json)

#partie 4 - analyse des données ======================================================================
melody = convert_temperature(temp, first_note, (personalize.lower() == "oui"))

#duration of main melody
melody_duration = duration(melody)
print("duration_melody = ", melody_duration)

# main melody
final_melody = temperature_and_chord(melody, melody_duration)
print("final_melody = ", final_melody)

#accompagning melody
instruments, accompagning  = convert_condition (condi,list_instruments)
print("instrument = ", instruments)
print("accompagning =", accompagning)
accompagning_duration = condition_duration(melody, condi, rainfall, wind, visibility, radiation)
print("duration_accomp = ", accompagning_duration)
generate_midi(final_melody, melody_duration, accompagning, accompagning_duration, instruments, freq, "test_neige.mid")