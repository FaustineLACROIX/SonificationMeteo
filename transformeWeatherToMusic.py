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

note_duration = [4,2,1,0.5,(1/3),0.25,0.125,0.0625] #ronde, blanche, noire, croche, triollet, double croche, triple croche, quadruple croche

# generate scale based on the first note
list_majeur = [2,2,1,2,2,2,1]
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

# generate list of data 
def convert_temperature(list):
    res = []
    scale_choosen = []
    temperature_min = min(list)
    temperature_max = max(list)

    # find the correct scale
    temperature_moy = sum(list)/len(list)

    if (temperature_moy < 5 ):
        scale_choosen = generate_scale(scale_winter,list_majeur)
    elif (temperature_moy < 12 ):
        scale_choosen = generate_scale(scale_autumn,list_majeur)
    elif (temperature_moy < 24):
        scale_choosen = generate_scale(scale_spring,list_majeur)
    else :
        scale_choosen = generate_scale(scale_summer,list_majeur)

    for temperature in list:
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
        res.append(chosen_note)

    return res

# temperature_list = [0, 7, 15, 28, 10, 20, 25, 2]
# notes = convert_temperature(temperature_list)
# print(notes)

# generate list of duration (modifie duration of the condition_list)
def convert_rainfall(list,note_duration):
    pass

# generate list of note with another instrument than for temperature
# param : list = list of string
def convert_condition(list,scale):
    pass

# generate list of duration 
def convert_wind(list,note_duration):
    pass

# generate one chord with the note composed of "number" note
def create_chord(note, number):
    pass