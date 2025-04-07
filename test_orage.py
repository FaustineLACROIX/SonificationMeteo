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
    "temperature_2m": [28.1, 28.3, 28.5, 28.1, 26.3, 26.5, 26.1, 28.3, 29.5, 32.1, 32.3, 28.5, 28.1, 28.3, 28.5],
    "weather_code": [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
    "precipitation": [50.0, 50.1, 50.2, 50.0, 50.1, 150.2, 150.0, 100.1, 100.2, 100.0, 100.1, 30.2,30.0, 30.1, 0.2],
    "wind_speed_10m": [20.5, 22.0, 23.5,20.5, 22.0, 23.5,20.5, 22.0, 23.5,20.5, 22.0, 23.5,20.5, 22.0, 23.5],
    "direct_radiation": [200, 250, 300,200, 250, 300,200, 250, 300,200, 250, 300,200, 250, 300],
    "visibility": [10000, 9500, 9000,10000, 9500, 9000,10000, 9500, 9000,10000, 9500, 9000,10000, 9500, 9000]
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
generate_midi(final_melody, melody_duration, accompagning, accompagning_duration, instruments, freq, "test_orage.mid")