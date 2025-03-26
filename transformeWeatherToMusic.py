import random
import numpy as np

from miditoolkit.midi import parser as mid_parser  
from miditoolkit.midi import containers as ct

# ========== MIDI =================================

# create an empty file
mido_obj = mid_parser.MidiFile()
beat_resol = mido_obj.ticks_per_beat

# create an  instrument
track = ct.Instrument(program=0, is_drum=False, name='example track')
mido_obj.instruments = [track]


# ========== DATA PARSING =========================
temperature_list = []
rainfall_list = []
condition_list = []
wind_list = []

# ========== DATA FOR MUSIC =======================
scale_winter = 60 # scale  ]-inf;5] 
scale_autumn = 60 # scale  ]5;12]
scale_spring = 60 # scale  ]12;24]
scale_summer = 60 # scale  ]24;+inf]

note_duration = [4, 2, 1, 0.5, (1/3), 0.25, 0.125, 0.0625] #ronde, blanche, noire, croche, triollet, double croche, triple croche, quadruple croche

# generate scale based on the first note
list_majeur = [2, 2, 1, 2, 2, 2, 1]
def generate_scale(scale, list):
    res = []
    res.append(scale)
    current_note = scale
    for i in range(len(list)):
        current_note = current_note + list[i]
        res.append(current_note)
    return res

# print(generate_scale(60,list_majeur))
 
# find the closest value in the list
def find_closest_value(value, list):
    return min(list, key=lambda note: abs(note - value))

# 1) TEMPERATURE TO SCALE ====================================================
# generate list of basique scale  
def convert_temperature(list_temp):
    list_scale = []
    scale_choosen = []
    temperature_min = min(list_temp)
    temperature_max = max(list_temp)

    # find the correct scale
    temperature_moy = sum(list_temp)/len(list_temp)

    if (temperature_moy < 5 ):
        scale_choosen = generate_scale(scale_winter,list_majeur)
    elif (temperature_moy < 12 ):
        scale_choosen = generate_scale(scale_autumn,list_majeur)
    elif (temperature_moy < 24):
        scale_choosen = generate_scale(scale_spring,list_majeur)
    else :
        scale_choosen = generate_scale(scale_summer,list_majeur)

    for temperature in list_temp:
        # Normalized temperature between 0 and 1
        if (temperature_max == temperature_min):
            normalized_temp = 0.5
        else :
            normalized_temp = (temperature - temperature_min)/(temperature_max - temperature_min)

        # interpolated the note
        note_min = scale_choosen[0]
        note_max = scale_choosen[-1]

        interpolated_note = note_min + normalized_temp * (note_max - note_min)

        # Find the closest note in the scale
        chosen_note = find_closest_value(interpolated_note,scale_choosen)

        # To add a little bit of random*
        if random.random() < 0.3:
            chosen_note = random.choice(scale_choosen)
        list_scale.append(chosen_note)

    return list_scale

# temperature_list = [0, 7, 15, 28, 10, 20, 25, 2]
# notes = convert_temperature(temperature_list)
# print(notes)

#2) CONDITION TO ADD AN OTHER INSTRUMENT =====================================
# generate list of note with another instrument than for temperature
# param : list = list of string
def convert_condition(list_condition,scale):
    for i in range (len(liste_condition)):
        if (liste_condition[i] == "Soleil"):
            # violon
            pass
        elif (liste_condition[i] == "Nuageux"):
            # ocrina 79
            pass
        elif (liste_condition[i] == "Brouillard"):
            # crystal 123
            pass
        elif (liste_condition[i] == "Pluie"):
            # drum synth 118
            pass
        elif (liste_condition[i] == "Neige"):
            # harpe 46
            pass
        else:
            # timpani 47
            pass
    pass

#3) RAINFALL TO SPEED OF DRUM ================================================
# generate list of duration (modifie duration of the condition_list)
def convert_rainfall(list_rainfall,note_duration):
    for i in range(len(list_rainfall)):
        # peu voir pas de précipitation
        if list_rainfall < 1:
            # un coup tous les blanches
            pass

        #pluie faible
        elif list_rainfall < 10:
            # un coup toute les noires
            pass

        #pluie modéré
        elif list_rainfall< 30:
            #un coup toutes les croches
            pass

        #pluie forte
        else:
            #un coup toutes les doubles crocher
            pass
    pass


#4) WIND TO SPEED OF ... =====================================================
# generate list of duration 
def convert_wind(list_wind,note_duration):
    list_duration = []
    for i in range(len(list_wind)):
        # air presque immobile
        if list_wind < 5:
            duration = rd.choices(note_durations, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration)

        #brise ressentie sur la peau
        elif list_wind < 20:
            duration = rd.choices(note_durations, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration)

        #sensation de vent présent
        elif list_wind< 50:
            duration = rd.choices(note_durations, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration)

        #vent fort et rafales
        else:
            duration = rd.choices(note_durations, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration)
    return list_duration


# generate list of duration 
def convert_visibility(list_visibility, note_duration):
    list_duration = []
    for i in range(len(list_visibility)):
        # aucune visibilité = fast
        if list_visibility[i] < 10:
            duration = rd.choices(note_durations, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration)

        # visibilité
        elif list_visibility[i] < 200:
            duration = rd.choices(note_durations, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration)

        #visibilité réduite
        elif list_visibility[i] < 500:
            duration = rd.choices(note_durations, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration)

        # visibilité
        else:
            duration = rd.choices(note_durations, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration)
        
    return list_duration

# generate list of duration 
def convert_radiation(list_radiation,note_duration):
    list_duration = []
    for i in range(len(list_radiation)):
        # lumière diffuse (matin, soir, pas de grand soleil)
        if list_radiation < 200:
            duration = rd.choices(note_durations, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration)

        # éclairage modéré, rayon de soleil, ciel partiellemnt dégagé
        elif list_radiation < 700:
            duration = rd.choices(note_durations, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration)

        # soleil présent, lunimosité
        elif list_radiation < 1000:
            duration = rd.choices(note_durations, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration)

        # lumière intense, plein soleil, midi
        else:
            duration = rd.choices(note_durations, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration)
    return list_duration

#5) CHORD LINK TO A NOTE =====================================================
# generate one chord with the note composed of "number" note
def create_chord(note, number):
    pass

#6) EVERY 3HOURS MAKE A CHORD ================================================


#7) CHOOSE DURATION =========================================================
def duration(list_temp, note_duration):
    duration_list = [] 
    for i in range(len(list_temp)):
        # blanche lors des accords tous les 3h
        if (i%3 == 0):
            duration_list.append(note_duration[1])
        #noir ou plus rapide répété pour que tous dure 1h    
        else:
            note_choose = rd.choices( note_duration, weights=[0, 0, 55, 25, 15, 4, 1 ], k=1)
            for i in range (int(1/note_choose)):
                duration_list.append(note_choose)
    return duration_list
                
