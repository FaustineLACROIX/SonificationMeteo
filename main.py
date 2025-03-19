from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

def city_wanted():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites le nom de la ville :")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=20)

    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + texte)
        return texte
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        print("Erreur de service ; {0}".format(e))


import os

def main():
    # partie 1 - introduction et ville souhaité
    text_intro = "Bonjour, je suis votre assistante Musical Weather. Vous voulez connaitre la météo de qu'elle ville aujourd'hui ?"
    tts = gTTS(text=text_intro, lang='fr')
    tts.save("introduction.mp3")
    playsound("introduction.mp3")
    city = city_wanted()

    # partie 2 - analyse et traitement des données
    text_traitement = f"D'accord, laissez moi quelques instant je vais vous joué la météo de {city}"
    tts = gTTS(text=text_traitement, lang='fr')
    tts.save("traitement.mp3")
    playsound("traitement.mp3")

    # # fetch
    # coord = convert_city_to_coordinate(city)
    # json_weather = fetch(coord)
    # temp = get_temperature(json)
    # wind = get_wind_speed(json)
    # rainfall = get_rainfall(json)
    # weather_cond = get_weather_conditions(json)

    # # parse
    # melody = convert_temperature_to_melody(temp)
    # melody_hour = add_harmonics_every_3hours(melody)
    # volume = convert_wind_speed_to_volume(wind)
    # rhythm = convert_rainfall_to_rhythm(rainfall)
    # stamp = convert_sky_condition_to_stamp(weather_cond)
    

main()
