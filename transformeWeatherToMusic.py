import random as rd
import numpy as np


# ========== DATA PARSING =========================
temperature_list = []
rainfall_list = []
condition_list = []
wind_list = []


# ========== DATA FOR MUSIC =======================
scale_winter = 59 # scale  ]-inf;5] Si
scale_autumn = 57 # scale  ]5;12] La 
scale_spring = 62 # scale  ]12;24] Re
scale_summer = 67 # scale  ]24;+inf] Sol
list_majeur = [2, 2, 1, 2, 2, 2, 1]

note_duration = [4, 2, 1, 0.5, (1/3), 0.25, 0.125, 0.0625] #ronde, blanche, noire, croche, triollet, double croche, triple croche, quadruple croche


# ========== DEFAULT SETTINGS ===================
def default_settings():
    freq = 1
    list_instruments = [40, 121, 44, 13, 46, 47]
    return freq, list_instruments


def generate_scale(scale, list):
    '''
    generate scale based on the first note and on list of different hight
    '''
    res = []
    res.append(scale)
    current_note = scale
    for i in range(len(list)):
        current_note = current_note + list[i]
        res.append(current_note)
    return res

## TESTS
# print(generate_scale(60,list_majeur))
 

# find the closest value in the list
def find_closest_value(val, lst):
    '''
    find the closest value of va in the list
    '''
    return min(lst, key=lambda x: abs(x - val))

# 1) TEMPERATURE TO SCALE ====================================================
#  
def convert_temperature(list_temp, note, isPersonalized):
    '''
    (called by main) generate list of basique scale
    param : list_temp list of temperate of the day
    note : starting note of the scale if isPersonalized true
    '''
    list_scale = []
    scale_choosen = []
    temperature_min = min(list_temp)
    temperature_max = max(list_temp)

    # find the correct scale
    temperature_moy = sum(list_temp)/len(list_temp)

    if (isPersonalized == 1):
        scale_choosen = generate_scale(note,list_majeur)
    elif (temperature_moy < 5 ):
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

        # To add a little bit of random
        if rd.random() < 0.3:
            chosen_note = rd.choice(scale_choosen)
        list_scale.append(chosen_note)

    return list_scale

#temperature_list = [0, 7, 15, 28, 10, 20, 25, 2]
#print ("moyenne =", (0+7+15+28+10+20+25+2)/8, ">12 donc gamme automne")
#notes = convert_temperature(temperature_list)
#print(notes)

#2) CONDITION TO ADD AN OTHER INSTRUMENT =====================================
# Create the 6 note mélodie 
def create_condition_melody(condition):
    '''
    Create the 6 note melody for accompagning
    param : condition the weather condition
    '''
    list_note = []
    if (condition == "Ensoleilé"):
        # violon
        list_note = [60, 62, 64, 67, 69, 71]

    elif (condition == "Nuageux"):
        # ocrina 79 X 121 
        list_note = [53, 50, 57, 59, 57, 59]
        #list_note = [55, 57, 60, 57, 60, 62]

     
    elif (condition == "Brumeux"):
        # trombone 58
        list_note = [36, 38, 43, 38, 41, 36]

    elif (condition == "Pluvieux"):
        # xylophone 13
        list_note = [50, 53, 57, 50, 53, 57]

    elif (condition == "Neigeux"):
        # harpe 46
        list_note = [83, 76, 79, 83, 74, 79]

    else:
        # timpani 47
        list_note = [31, 31, 34, 31, 31, 34]
        
    # retourne tab de 6 notes/accords 
    return list_note



def convert_condition(list_condition, list_instru):
    '''
    (called by main)
    construct the list of note for accompagning and list of instrument which is associate to each note
    param : list_condition = list of string 
    param : list_instru = contained midi number of instrument for every weather conditions
    '''
    
    conditions = ["Ensoleilé", "Nuageux", "Brumeux", "Pluvieux", "Neigeux", "Orageux"]
    # create list_melody inside function
    list_melody = []
    for i in conditions:
        list_melody.append(create_condition_melody(i))
     
    list_note = []
    list_final_instru = []
    previous = list_condition[0]
    i=0

    # throught all weather condition of the day
    for ind in range(len(list_condition)):
        
        # find the corresponding index of conditions
        condition_index = conditions.index(list_condition[ind])

        if (conditions[condition_index] == previous):
            list_final_instru.append(list_instru[condition_index])
            note = list_melody[condition_index][i % len(list_melody[condition_index])]
            list_note.append(note)
            i += 1

        else :
            i = 0
            list_final_instru.append(list_instru[condition_index])
            note = list_melody[condition_index][i]
            list_note.append(note)

        previous = conditions[condition_index]

    return list_final_instru, list_note


# 3) Preparation DURATION LIST FOR ACCOMPAGNEMENT ================================================
# 3.1) RAINFALL TO SPEED OF DRUM 
def convert_rainfall(list_rainfall):
    '''
    (intern called)
    generate list of duration for rain, snow and orage conditions
    param : list_rainfall = list of float
    '''
    list_duree = []
    for i in range(len(list_rainfall)):
        # peu voir pas de précipitation
        if list_rainfall[i] < 1:
            # proba 70% sur blanche ronde / 20% noir / 10% au dessus
            duration = rd.choices(note_duration, weights=[35,35,26,2,2,0,0,0], k=1)
            list_duree.append(duration[0])
     

        #pluie faible
        elif list_rainfall[i] < 10:
            # proba 15% ronde pareil blanche, 20% noir, 10% croche et le reste
            duration = rd.choices(note_duration, weights=[15,25,35,15,5,5,0,0], k=1)
            list_duree.append(duration[0])
           

        #pluie modéré
        elif list_rainfall[i] < 30:
            # proba 0 ronde 20% blanche, 40%noir, 20%croche
            duration = rd.choices(note_duration, weights=[0,5,40,30,10,10,5,0], k=1)
            list_duree.append(duration[0])

        #pluie forte
        else:
            # proba 0 ronde/blanche 10%noire, 20%croche 
            duration = rd.choices(note_duration, weights=[0,0,10,20,30,25,10,5], k=1)
            list_duree.append(duration[0])
    # retourne tab de duréé (longueur = len(list_rainfall))
    return list_duree



# 3.2) WIND TO SPEED OF CLOUD
#  
def convert_wind(list_wind):
    '''
    (intern called)
    generate list of duration for cloud condition
    param : list_wind = list of float
    '''
    list_duration = []
    for i in range(len(list_wind)):
        # air presque immobile
        if list_wind[i] < 5:
            duration = rd.choices(note_duration, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration[0])

        #brise ressentie sur la peau
        elif list_wind[i] < 20:
            duration = rd.choices(note_duration, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration[0])

        #sensation de vent présent
        elif list_wind[i]< 50:
            duration = rd.choices(note_duration, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration[0])

        #vent fort et rafales
        else:
            duration = rd.choices(note_duration, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration[0])
    return list_duration

# 3.3) VISIBILITY TO SPEED OF MIST
def convert_visibility(list_visibility):
    '''
    (intern called)
    generate list of duration for mist condition
    param : list_visibility = list of float
    '''
    list_duration = []
    for i in range(len(list_visibility)):
        # aucune visibilité = fast
        if list_visibility[i] < 10:
            duration = rd.choices(note_duration, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration[0])

        # visibilité
        elif list_visibility[i] < 200:
            duration = rd.choices(note_duration, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration[0])

        #visibilité réduite
        elif list_visibility[i] < 500:
            duration = rd.choices(note_duration, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration[0])

        # visibilité
        else:
            duration = rd.choices(note_duration, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration[0])
        
    return list_duration

# 3.4) RADIATION TO SPEED OF SUN
def convert_radiation(list_radiation):
    '''
    (intern called)
    generate list of duration for sunny condition
    param : list_radiation = list of float
    '''
    list_duration = []
    for i in range(len(list_radiation)):
        # lumière diffuse (matin, soir, pas de grand soleil)
        if list_radiation[i] < 200:
            duration = rd.choices(note_duration, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration[0])

        # éclairage modéré, rayon de soleil, ciel partiellemnt dégagé
        elif list_radiation[i] < 700:
            duration = rd.choices(note_duration, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration[0])

        # soleil présent, lunimosité
        elif list_radiation[i] < 1000:
            duration = rd.choices(note_duration, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration[0])

        # lumière intense, plein soleil, midi
        else:
            duration = rd.choices(note_duration, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration[0])
    return list_duration


# 3.5)SPEED OF STORM
def convert_storm(list_rainfall):
    '''
    (intern called)
    generate list of duration for strom
    param : no very important juste need size
    '''
    list_duration = []

    for i in range(int(len(list_rainfall)/3)):
        list_duration.append(0.5)
        list_duration.append(0.5)
        list_duration.append(1)


    return list_duration

#5) CHORD LINK TO A NOTE =====================================================
# 
def create_chord(note):
    '''
    (intern called)
    generate one chord with the note composed of 5 note
    param : note of the based of the chord
    '''
    intervals = [0, 4, 7]
    chord = []
    for i in intervals:
        chord.append(note + i)
    return chord

#6) EVERY 3HOURS MAKE A CHORD ================================================
# Mettre la liste des notes avec l'accord tous les 3h 
def temperature_and_chord(list_temp, duration_list):
    '''
    (called by main)
    create final melody including chord each 3 hours
    param : list_temp = list from function convert_temperature
    '''
    list_temp_final = []
    j=0
    for i in range(len(list_temp)):
        # ajout accord (3h)
        if (i%(12) == 0):
            list_temp_final.append(create_chord(list_temp[i]))
            j += 1
     
        # ajout des notes 
        else:
            #if duration_list[j] < 1:
            #    for _ in range(int(1/duration_list[j])):
            #        list_temp_final.append(list_temp[i])
            #    j += int(1/duration_list[j])
            #else:
            list_temp_final.append(list_temp[i]) 
            #    j += 1
         

    return list_temp_final

#7) CHOOSE DURATION =========================================================
# durée :  pas de blanche et ronde et si croche ou autre note répétter pour
# faire le temps d'une noire pour la température 
def duration(list_temp):
    '''
    (called by main)
    create melody duration
    param : list_temp = list from function convert_temperature
    '''
    duration_list = [] 
    for i in range(len(list_temp)):
        # blanche lors des accords tous les 3h
        if (i%(12) == 0):
            duration_list.append(note_duration[2])
        #noir ou plus rapide répété pour que tous dure 1h    
        else:
            note_choose = rd.choices( note_duration, weights=[0, 0, 60, 28, 11, 1, 0, 0 ], k=1)
            #for _ in range (int(1/note_choose[0])):
            #    duration_list.append(note_choose[0])
            duration_list.append(note_choose[0])

    return duration_list
                


def condition_duration(list_note, list_condi, data_rainfall, data_wind, data_visibility, data_radiation):
    '''
    (called by main)
    create final duration for accompagning
    param : list_note = list from function convert_temperature for its lenght
    param : list_condition = list of all weather condition of the day
    '''
    list_duration = [] # final duration list
    
    #Apply fonction to convert api data in list of duration
    list_radiation = convert_radiation(data_radiation)
    list_wind = convert_wind(data_wind)
    list_visibility = convert_visibility(data_visibility)
    list_rainfall = convert_rainfall(data_rainfall)
    list_snow = convert_rainfall(data_rainfall)
    list_storm = convert_storm(data_rainfall)


    for i in range(len(list_note)):

        if (list_condi[i]== "Ensoleilé"):
            list_duration.append(list_radiation[i])
        
        elif (list_condi[i] == "Nuageux"):
            list_duration.append(list_wind[i])
        
        elif (list_condi[i] == "Brumeux"):
            list_duration.append(list_visibility[i])

        elif (list_condi[i] == "Pluvieux"):
            list_duration.append(list_rainfall[i])

        elif (list_condi[i] == "Neigeux"):
            list_duration.append(list_snow[i])

        elif (list_condi[i] == "Orageux"):
            list_duration.append(list_storm[i])

    return list_duration
