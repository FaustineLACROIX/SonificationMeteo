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
scale_winter = 0 # scale 
scale_autumn = 0 # scale
scale_spring = 0 # scale
scale_summer = 0 # scale

note_duration = [4,2,1,0.5,(1/3),0.25,0.125,0.0625] #ronde, blanche, noire, croche, triollet, double croche, triple croche, quadruple croche

# generate scale based on the first note
def generate_scale(scale):
    pass

# generate list of data 
def convert_temperature(list,scale):
    pass

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