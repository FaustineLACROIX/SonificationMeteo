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
    "temperature_2m": [20.1, 20.3, 20.4,20.1, 20.3, 20.4,16.1, 16.3, 16.4,12.1, 12.3, 10.4,12.1, 12.3, 17.4],
    "weather_code": [51, 51, 51,51, 51, 51,51, 51, 51,51, 51, 51,51, 51, 51],
    "precipitation": [0.1, 0.1, 0.2,10,10,10,30,30,30,10,50,50,50,50,50],
    "wind_speed_10m": [5.1, 5.3, 5.5,5.1, 5.3, 5.5,5.1, 5.3, 5.5,5.1, 5.3, 5.5,5.1, 5.3, 5.5],
    "direct_radiation": [100, 120, 130,100, 120, 130,100, 120, 130,100, 120, 130,100, 120, 130],
    "visibility": [15000, 14000, 13000,15000, 14000, 13000,15000, 14000, 13000,15000, 14000, 13000,15000, 14000, 13000]
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
generate_midi(final_melody, melody_duration, accompagning, accompagning_duration, instruments, freq, "test_pluie.mid")