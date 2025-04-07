from generateMidi import *

freq = 1
#V1 note se répète pour duré 1 temps
duration_melody =  [2, 1, 1, 0.5, 0.5, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 2, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 1, 1, 2, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 0.5, 0.5, 0.5, 0.5, 2, 0.5, 0.5, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 0.5, 0.5, 1, 0.5, 0.5, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.25, 0.25, 0.25, 0.25, 2, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.25, 0.25, 0.25, 0.25, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 2, 1, 1, 0.5, 0.5, 1, 0.5, 0.5, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 1]
final_melody =  [[91, 95, 98, 101, 105], 91, 91, 91, 91, 91, 91, 91, 91, 81, 91, 91, 91, 91, 91, 91, 91, 91, 90, [91, 95, 98, 101, 105], 88, 88, 88, 91, 91, 91, 91, 91, 91, 84, 91, 91, 91, 88, 91, 81, 88, 88, 88, 88, [88, 92, 95, 98, 102], 88, 88, 91, 91, 86, 86, 91, 91, 91, 91, 91, 88, 88, 88, 88, 86, 84, [88, 92, 95, 98, 102], 84, 84, 84, 83, 83, 83, 79, 79, 90, 79, 79, 79, 79, 79, 79, 83, 83, [83, 87, 90, 93, 97], 83, 83, 88, 88, 88, 88, 90, 88, 88, 79, 83, 83, 91, 91, 90, 90, 90, 91, 91, 91, 91, [91, 95, 98, 101, 105], 91, 83, 90, 90, 90, 91, 91, 91, 91, 79, 91, 91, 83, 79, 91, 91, [91, 95, 98, 101, 105], 91, 91, 91, 91, 91, 91, 88, 88, 88, 88, 83, 83, 83, 81, 83, 83, 83, [83, 87, 90, 93, 97], 83, 83, 79, 79, 91, 79, 79, 79, 79, 79, 79, 90, 90, 90, 90, 79, 79, 79, 79, 90]
instrument =  [79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 40, 40, 40, 40, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 40, 40, 40, 40, 40, 40, 40, 40, 79, 79, 79, 79, 40, 40, 40, 40, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79]
accompagning = [55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 60, 60, 62, 64, 55, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 60, 60, 62, 64, 67, 69, 71, 60, 55, 55, 57, 60, 60, 60, 62, 64, 55, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62]
duration_accomp =  [1, 0.5, 0.3333333333333333, 0.5, 1, 0.3333333333333333, 0.5, 0.5, 0.5, 0.5, 2, 1, 0.5, 2, 0.5, 0.5, 0.5, 0.5, 0.3333333333333333, 0.5, 0.5, 0.5, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.3333333333333333, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.3333333333333333, 0.5, 1, 0.5, 0.5, 0.3333333333333333, 0.5, 0.5, 0.3333333333333333, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 2, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 0.5, 0.5, 1, 1, 0.3333333333333333, 0.5, 0.3333333333333333, 1, 0.5, 1, 1, 1, 1, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 0.5, 0.3333333333333333]

generate_midi(final_melody, duration_melody, accompagning, duration_accomp, instrument, freq, "test_midi_repet.mid")

#V2 note ne se répète pas
duration_melody =  [2, 1, 1, 1, 1, 0.5, 0.5, 0.3333333333333333, 0.5, 0.5, 0.3333333333333333, 0.5, 2, 1, 0.5, 0.5, 0.25, 0.5, 0.5, 1, 1, 1, 0.3333333333333333, 1, 2, 1, 0.5, 0.3333333333333333, 1, 1, 1, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 0.3333333333333333, 2, 1, 0.5, 0.5, 1, 1, 0.3333333333333333, 1, 1, 0.5, 0.5, 1, 2, 0.5, 1, 0.5, 1, 1, 1, 0.3333333333333333, 1, 1, 1, 1, 2, 1, 0.5, 1, 1, 1, 0.5, 0.5, 0.25, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1, 0.5, 0.3333333333333333, 0.5, 1, 0.5, 2, 0.3333333333333333, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1]
final_melody =  [[91, 93, 95], 84, 81, 91, 91, 91, 91, 91, 91, 91, 91, 91, [91, 93, 95], 91, 88, 91, 84, 88, 81, 91, 91, 91, 88, 88, [88, 90, 92], 88, 88, 91, 91, 91, 91, 79, 88, 88, 88, 88, [84, 86, 88], 84, 84, 83, 83, 83, 79, 81, 91, 84, 79, 83, [83, 85, 87], 90, 83, 84, 88, 88, 91, 91, 91, 90, 91, 91, [84, 86, 88], 91, 91, 91, 84, 91, 81, 91, 91, 91, 91, 91, [91, 93, 95], 91, 84, 91, 91, 81, 88, 86, 84, 83, 83, 79, [79, 81, 83], 83, 83, 88, 79, 90, 86, 79, 79, 79, 79, 79]
instrument =  [79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 40, 40, 40, 40, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 40, 40, 40, 40, 40, 40, 40, 40, 79, 79, 79, 79, 40, 40, 40, 40, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79]
accompagning = [55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 60, 60, 62, 64, 55, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 60, 60, 62, 64, 67, 69, 71, 60, 55, 55, 57, 60, 60, 60, 62, 64, 55, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62, 65, 67, 55, 57, 60, 62]
duration_accomp =  [0.3333333333333333, 0.5, 0.5, 0.5, 0.3333333333333333, 0.5, 0.5, 0.3333333333333333, 1, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 0.5, 0.3333333333333333, 0.5, 1, 0.5, 0.5, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.3333333333333333, 0.5, 1, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 0.5, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.3333333333333333, 1, 0.3333333333333333, 0.3333333333333333, 0.5, 1, 0.5, 1, 1, 0.5, 0.5, 0.5, 0.3333333333333333, 2, 1, 0.5, 0.3333333333333333, 0.5, 1, 0.3333333333333333, 0.5, 0.5, 1]




generate_midi(final_melody, duration_melody, accompagning, duration_accomp, instrument, freq, "test_midi_once.mid")
    
# https://api.open-meteo.com/v1/forecast?latitude=44.8404&longitude=-0.5805&hourly=temperature_2m&minutely_15=temperature_2m,precipitation,wind_speed_80m,visibility,direct_radiation&start_date=2025-04-14&end_date=2025-04-14