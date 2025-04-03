import random
import numpy as np
from miditoolkit.midi import parser as mid_parser  
from miditoolkit.midi import containers as ct

# Definition of note and duration lists
list_temp = []
list_temp_duration = []
list_note_condition = []
list_instru = []
list_duration_condition = []

# Create an empty MIDI file
midi_obj = mid_parser.MidiFile()
beat_resol = midi_obj.ticks_per_beat

# Create a track for the piano
piano_track = ct.Instrument(program=0, is_drum=False, name='Piano')
instrument_tracks = {}  # Dictionary to store tracks by instrument

# Current time (not playing the next note before or during the current)
current_time = 0  

# Play temperature notes with the piano
for i in range(len(list_temp)):
    note = list_temp[i]
    duration = list_temp_duration[i]
    piano_track.notes.append(ct.Note(start=current_time, end=current_time + duration, pitch=note, velocity=80))
    current_time += duration  


# Reset time to start from 0 for condition notes
current_time = 0  

# Play weather condition notes with their instruments
for i in range(len(list_note_condition)):
    note = list_note_condition[i]
    instr = list_instru[i]
    duration = list_duration_condition[i]
    
    # Create track only if it doesn't exist
    if instr not in instrument_tracks:
        instrument_tracks[instr] = ct.Instrument(program=instr, is_drum=False, name=f'Instrument_{instr}')
    
    # Add note to the correct instrument track
    instrument_tracks[instr].notes.append(ct.Note(start=current_time, end=current_time + duration, pitch=note, velocity=80))
    current_time += duration  

# Add track to the final midi_obj
midi_obj.instruments.append(piano_track)
midi_obj.instruments.extend(instrument_tracks.values())

# Save the generated MIDI file
midi_obj.dump("weather_melody.mid")
