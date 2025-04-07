from interface import Application
from fetchAndParseAPI import *
from transformeWeatherToMusic import *

app = Application()
app.mainloop()
city, first_note, freq, list_instruments = app.get_settings()
coord = convert_city_to_coordinate(city)
personalize = "oui"

#partie 3 - cherches les informations sur l'api =======================================================
json = fetch(coord)
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