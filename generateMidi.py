import random
import numpy as np
from miditoolkit.midi import parser as mid_parser  
from miditoolkit.midi import containers as ct

# Definition of note and duration lists


def generate_midi(melody, melody_duration, accompagning,
                  condition_duration, instruments, 
                  freq, title = "weather_melody_test.mid"):
    # Create an empty MIDI file
    midi_obj = mid_parser.MidiFile()
    beat_resol = midi_obj.ticks_per_beat

    # Create a track for the piano
    piano_track = ct.Instrument(program=24, is_drum=False, name='Piano')
    instrument_tracks = {}  # Dictionary to store tracks by instrument

    # Current time (not playing the next note before or during the current)
    current_time = 0  

    # Play temperature notes with the piano
    for i in range(int(len(melody)/freq)):
        note = melody[i*freq]
        #print("note",note)
        duration = int(beat_resol * melody_duration[i*freq])
        #print("duration",duration)

        if isinstance(note, list):
            for sub in note:
                #print("sub:", sub, type(sub))  # Debug
                piano_track.notes.append(ct.Note(start=current_time, end=current_time + duration, pitch=int(sub), velocity=100))
        else:
            #print("note:", note, type(note))  # Debug
            piano_track.notes.append(ct.Note(start=current_time, end=current_time + duration, pitch=int(note), velocity=90))
        current_time += duration 
        #print("current_time",current_time) 


    # Reset time to start from 0 for condition notes
    current_time = 0  

    # Play weather condition notes with their instruments
    for i in range(int(len(accompagning)/freq)):
        note = accompagning[i*freq]
        instr = instruments[i*freq]
        duration = int(beat_resol *condition_duration[i*freq])

        # Create track only if it doesn't exist
        if instr not in instrument_tracks:
            instrument_tracks[instr] = ct.Instrument(program=instr, is_drum=False, name=f'Instrument_{instr}')

        # Add note to the correct instrument track
        instrument_tracks[instr].notes.append(ct.Note(start=current_time, end=current_time + duration, pitch=note, velocity=50))
        current_time += duration  

    # Add track to the final midi_obj
    midi_obj.instruments.append(piano_track)
    midi_obj.instruments.extend(instrument_tracks.values())


    # Debug avant d'appeler midi_obj.dump()
    #print("Instruments:", midi_obj.instruments)
    #for instrument in midi_obj.instruments:
    #    for note in instrument.notes:
    #        print(f"Note: {note.pitch}, Start: {note.start}, End: {note.end}, Velocity: {note.velocity}")

    # Save the generated MIDI file
    midi_obj.dump(title)
