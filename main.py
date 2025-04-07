import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from interface import Application
from fetchAndParseAPI import *
from transformeWeatherToMusic import *
from generateMidi import *

def response(string):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(string)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=20)

    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + texte)
        return texte
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        print("Erreur de service ; {0}".format(e))
    

def main():
    # partie 1 - introduction et ville souhaité ==========================================================
    text_intro = "Bonjour"
    suit =", je suis votre assistante Musical Weather. Mon but est de vous guidé pour crée une musique qui exprime la météo du jour. Voulez-vous personalisé cette musique?"
    tts = gTTS(text=text_intro, lang='fr')
    tts.save("introduction.mp3")
    playsound("introduction.mp3")
    personalize = response("Dites oui pour personnaliser cette musique, sinon dite non")

    city = "Paris"
    
    if personalize == "oui" :
        app = Application()
        app.mainloop()
        city, first_note, freq, list_instruments = app.get_settings()
        coord = convert_city_to_coordinate(city)

    else :
        text_ville = "Vous voulez la météo de qu'elle ville aujourd'hui ?"
        tts = gTTS(text=text_ville, lang='fr')
        tts.save("ville.mp3")
        playsound("ville.mp3")
        city = response("Dites le nom de la ville voulue")
        coord = convert_city_to_coordinate(city)
        first_note = 0
        freq, list_instruments = default_settings()


    
        
    #partie 2 - analyse et traitement des données ========================================================
    text_traitement = f"D'accord, laissez moi quelques instant je vais vous joué la météo de {city}"
    tts = gTTS(text=text_traitement, lang='fr')
    tts.save("traitement.mp3")
    playsound("traitement.mp3")


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

    #partie 5 - génération du fichier MIDI ===============================================================
    generate_midi(final_melody, melody_duration, accompagning, accompagning_duration, instruments, freq, "weather.mid")
    


if __name__ == "__main__":
    main()

