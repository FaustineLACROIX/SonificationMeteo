import random as rd
import numpy as np


# ========== DATA PARSING =========================
temperature_list = []
rainfall_list = []
condition_list = []
wind_list = []


# ========== DATA FOR MUSIC =======================
scale_winter = 47 # scale  ]-inf;5] Si
scale_autumn = 45 # scale  ]5;12] La 
scale_spring = 74 # scale  ]12;24] Re
scale_summer = 79 # scale  ]24;+inf] Sol

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
def convert_temperature(list_temp,note, isPersonalized=0):
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

# temperature_list = [0, 7, 15, 28, 10, 20, 25, 2]
# notes = convert_temperature(temperature_list)
# print(notes)

#2) CONDITION TO ADD AN OTHER INSTRUMENT =====================================
# Create the 6 note mélodie 
def create_condition_melody(condition):
    list_note = []
    if (condition == "Ensoleilé"):
        # violon
        list_note = [60,62,64,67,69,71]

    elif (condition == "Nuageux"):
        # ocrina 79
        list_note = [55, 57, 60, 62, 65, 67]
     
    elif (condition == "Brumeux"):
        # trombone 58
        list_note = [36, 38, 41, 43, 46, 48]

    elif (condition == "Pluvieux"):
        # xylophone 13
        list_note = [45, 47, 50, 52, 54, 57]

    elif (condition == "Neigeux"):
        # harpe 46
        list_note = [40, 42, 45, 47, 50, 52]

    else:
        # timpani 47
        list_note = [35, 37, 40, 42, 45, 47]
        
    # retourne tab de 6 notes/accords 
    return list_note



# generate list of note with another instrument than for temperature
# param : list = list of string / list_melody = contained the melody for each condition
def convert_condition(list_condition, list_melody, list_instru=[40, 79, 58, 13, 46, 47]):
    
    conditions = ["Ensoleilé", "Nuageux", "Brumeux", "Pluvieux", "Neigeux", "Orageux"]
    
    index_list = [0] * len(conditions) # list d'index pour identifier ou on en est dans la mélodie

    last_condition = None  
    list_note = []
    list_final_instru = []

    for condition in list_condition:
        
        condition_index = conditions.index(condition)

        # Réinitialisation des index si la condition change
        if condition != last_condition:
            index_list = [0] * len(conditions)

       
        note = list_melody[condition_index][index_list[condition_index] % len(list_melody[condition_index])]
        list_note.append(note)
        list_final_instru.append(list_instru[condition_index])

        
        index_list[condition_index] += 1  

        last_condition = condition  

    return list_final_instru, list_note


#3) RAINFALL TO SPEED OF DRUM ================================================
# generate list of duration (modifie duration of the condition_list)
def convert_rainfall(list_rainfall,note_duration):
    list_duree = []
    for i in range(len(list_rainfall)):
        # peu voir pas de précipitation
        if list_rainfall[i] < 1:
            # proba 70% sur blanche ronde / 20% noir / 10% au dessus
            list_duree.append(rd.choice((note_duration), weigths=[35,35,26,2,2,0,0,0], k=1))
     

        #pluie faible
        elif list_rainfall[i] < 10:
            # proba 15% ronde pareil blanche, 20% noir, 10% croche et le reste
            list_duree.append(rd.choice((note_duration), weigths=[15,25,35,15,5,5,0,0], k=1))
           

        #pluie modéré
        elif list_rainfall[i] < 30:
            # proba 0 ronde 20% blanche, 40%noir, 20%croche
            list_duree.append(rd.choice((note_duration), weigths=[0,5,40,30,10,10,5,0], k=1))

        #pluie forte
        else:
            # proba 0 ronde/blanche 10%noire, 20%croche 
            list_duree.append(rd.choice((note_duration), weigths=[0,0,10,20,30,25,10,5], k=1))
    # retourne tab de duréé (longueur = len(list_rainfall))
    return list_duree



#4) WIND TO SPEED OF ... =====================================================
# generate list of duration 
def convert_wind(list_wind,note_duration):
    list_duration = []
    for i in range(len(list_wind)):
        # air presque immobile
        if list_wind[i] < 5:
            duration = rd.choices(note_duration, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration)

        #brise ressentie sur la peau
        elif list_wind[i] < 20:
            duration = rd.choices(note_duration, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration)

        #sensation de vent présent
        elif list_wind[i]< 50:
            duration = rd.choices(note_duration, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration)

        #vent fort et rafales
        else:
            duration = rd.choices(note_duration, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration)
    return list_duration


# generate list of duration 
def convert_visibility(list_visibility, note_duration):
    list_duration = []
    for i in range(len(list_visibility)):
        # aucune visibilité = fast
        if list_visibility[i] < 10:
            duration = rd.choices(note_duration, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration)

        # visibilité
        elif list_visibility[i] < 200:
            duration = rd.choices(note_duration, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration)

        #visibilité réduite
        elif list_visibility[i] < 500:
            duration = rd.choices(note_duration, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration)

        # visibilité
        else:
            duration = rd.choices(note_duration, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration)
        
    return list_duration

# generate list of duration 
def convert_radiation(list_radiation,note_duration):
    list_duration = []
    for i in range(len(list_radiation)):
        # lumière diffuse (matin, soir, pas de grand soleil)
        if list_radiation[i] < 200:
            duration = rd.choices(note_duration, weights=[0, 55, 35, 10, 5, 0, 0, 0], k=1)
            list_duration.append(duration)

        # éclairage modéré, rayon de soleil, ciel partiellemnt dégagé
        elif list_radiation[i] < 700:
            duration = rd.choices(note_duration, weights=[0, 2, 23, 53, 20, 2, 0, 0], k=1)
            list_duration.append(duration)

        # soleil présent, lunimosité
        elif list_radiation[i] < 1000:
            duration = rd.choices(note_duration, weights=[0, 0, 2, 11, 22, 50, 15, 0], k=1)
            list_duration.append(duration)

        # lumière intense, plein soleil, midi
        else:
            duration = rd.choices(note_duration, weights=[0, 0, 0, 0, 5, 10, 35, 50], k=1)
            list_duration.append(duration)
    return list_duration


# TO DO
def convert_snow(list_, note_duration):
    pass

def convert_storm(list_, note_duration):
    pass

#5) CHORD LINK TO A NOTE =====================================================
# generate one chord with the note composed of 5 note
def create_chord(note):
    intervals = [0, 4, 7, 10, 14]
    chord = []
    for i in intervals:
        chord.append(note + i)
    return chord

#6) EVERY 3HOURS MAKE A CHORD ================================================


#7) CHOOSE DURATION =========================================================
# durée :  pas de blanche et ronde et si croche ou autre note répétter pour faire le temps d'une noire
# pour la température 
def duration(list_temp, note_duration, freq=1):
    duration_list = [] 
    for i in range(len(list_temp)):
        # blanche lors des accords tous les 3h
        if (i%(12/freq) == 0):
            duration_list.append(note_duration[1])
        #noir ou plus rapide répété pour que tous dure 1h    
        else:
            note_choose = rd.choices( note_duration, weights=[0, 0, 55, 25, 15, 4, 1 ], k=1)
            for i in range (int(1/note_choose)):
                duration_list.append(note_choose)
    return duration_list
                


#8) Mettre la liste des notes avec l'accord tous les 3h
# param : list_temp : list issus de la fonction convert temperature 
def temperature_and_chord(list_temp):
    list_temp_final = []
    for i in range(len(list_temp)):
        # ajout accord (3h)
        if (i%(12/freq) == 0):
            list_temp_final.append(create_chord(list_temp[i]))
        # ajout des notes 
        list_temp_final.append(list_temp[i])


    return list_temp_final

def find_condition(instru, list_instru):
    if (instru == list_instru[0]):
        return "Ensoleilé"

    elif (instru == list_instru[1]):
        return "Nuageux"
     
    elif (instru == list_instru[2]):
        return "Brumeux"

    elif (instru == list_instru[3]):
        return "Pluvieux"

    elif (instru == list_instru[4]):
        return "Neigeux"

    else:
        return "Orageux"
        

#9) Fonction : mettre bonne durée pour chaque note de condition méthéo

def condition_duration(list_note, list_instru, data_rainfall, data_wind, data_visibility, data_radiation, data_snow, data_storm):
    list_duration = [] # final duration list
    
    #Apply fonction to convert api data in list of duration
    list_radiation = convert_radiation(data_radiation,note_duration)
    list_wind = convert_wind(data_wind, note_duration)
    list_visibility = convert_visibility(data_visibility,note_duration)
    list_rainfall = convert_rainfall(data_rainfall,note_duration)
    list_snow = convert_snow(data_snow, note_duration)
    list_storm = convert_storm(data_storm, note_duration)


    for i in range(len(list_note)):

        if (find_condition(list_instru[i],list_instru) == "Ensoleilé"):
            list_duration.append(list_radiation[i])
        
        elif (find_condition(list_instru[i],list_instru) == "Nuageux"):
            list_duration.append(list_wind[i])
        
        elif (find_condition(list_instru[i],list_instru) == "Brumeux"):
            list_duration.append(list_visibility[i])

        elif (find_condition(list_instru[i],list_instru) == "Pluvieux"):
            list_duration.append(list_rainfall[i])

        elif (find_condition(list_instru[i],list_instru) == "Neigeux"):
            list_duration.append(list_snow[i])

        elif (find_condition(list_instru[i],list_instru) == "Orageux"):
            list_duration.append(list_storm[i])

    return list_duration