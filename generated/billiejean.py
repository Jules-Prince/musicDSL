from midiutil import MIDIFile
midi = MIDIFile(2)
midi.addTempo(0, 0, 118)
time_signature = ( 4 ,  4 )
midi.addTimeSignature(0, 0, *time_signature, 24)
midi.addProgramChange(0, 0, 0, 9)
midi.addNote(0, 9, 42,0 , 1.0, 90)
midi.addNote(0, 9, 36,0 , 1.0, 90)
midi.addNote(0, 9, 42,0.5 , 1.0, 90)
midi.addNote(0, 9, 38,1 , 1.0, 90)
midi.addNote(0, 9, 42,1 , 1.0, 90)
midi.addNote(0, 9, 42,1.5 , 1.0, 90)
midi.addNote(0, 9, 36,2 , 1.0, 95)
midi.addNote(0, 9, 42,2 , 1.0, 95)
midi.addNote(0, 9, 42,2.5 , 1.0, 95)
midi.addNote(0, 9, 38,3 , 1.0, 90)
midi.addNote(0, 9, 42,3 , 1.0, 95)
midi.addNote(0, 9, 42,3.5 , 1.0, 95)
midi.addNote(0, 9, 42,4 , 1.0, 90)
midi.addNote(0, 9, 36,4 , 1.0, 90)
midi.addNote(0, 9, 42,4.5 , 1.0, 90)
midi.addNote(0, 9, 38,5 , 1.0, 90)
midi.addNote(0, 9, 42,5 , 1.0, 90)
midi.addNote(0, 9, 42,5.5 , 1.0, 90)
midi.addNote(0, 9, 36,6 , 1.0, 95)
midi.addNote(0, 9, 42,6 , 1.0, 95)
midi.addNote(0, 9, 42,6.5 , 1.0, 95)
midi.addNote(0, 9, 38,7 , 1.0, 90)
midi.addNote(0, 9, 42,7 , 1.0, 95)
midi.addNote(0, 9, 42,7.5 , 1.0, 95)
midi.addNote(0, 9, 42,8 , 1.0, 90)
midi.addNote(0, 9, 36,8 , 1.0, 90)
midi.addNote(0, 9, 42,8.5 , 1.0, 90)
midi.addNote(0, 9, 38,9 , 1.0, 90)
midi.addNote(0, 9, 42,9 , 1.0, 90)
midi.addNote(0, 9, 42,9.5 , 1.0, 90)
midi.addNote(0, 9, 36,10 , 1.0, 95)
midi.addNote(0, 9, 42,10 , 1.0, 95)
midi.addNote(0, 9, 42,10.5 , 1.0, 95)
midi.addNote(0, 9, 38,11 , 1.0, 90)
midi.addNote(0, 9, 42,11 , 1.0, 95)
midi.addNote(0, 9, 42,11.5 , 1.0, 95)
midi.addNote(0, 9, 42,12 , 1.0, 90)
midi.addNote(0, 9, 36,12 , 1.0, 90)
midi.addNote(0, 9, 42,12.5 , 1.0, 90)
midi.addNote(0, 9, 38,13 , 1.0, 90)
midi.addNote(0, 9, 42,13 , 1.0, 90)
midi.addNote(0, 9, 42,13.5 , 1.0, 90)
midi.addNote(0, 9, 36,14 , 1.0, 95)
midi.addNote(0, 9, 42,14 , 1.0, 95)
midi.addNote(0, 9, 42,14.5 , 1.0, 95)
midi.addNote(0, 9, 38,15 , 1.0, 90)
midi.addNote(0, 9, 42,15 , 1.0, 95)
midi.addNote(0, 9, 42,15.5 , 1.0, 95)
midi.addNote(0, 9, 42,16 , 1.0, 90)
midi.addNote(0, 9, 36,16 , 1.0, 90)
midi.addNote(0, 9, 42,16.5 , 1.0, 90)
midi.addNote(0, 9, 38,17 , 1.0, 90)
midi.addNote(0, 9, 42,17 , 1.0, 90)
midi.addNote(0, 9, 42,17.5 , 1.0, 90)
midi.addNote(0, 9, 36,18 , 1.0, 95)
midi.addNote(0, 9, 42,18 , 1.0, 95)
midi.addNote(0, 9, 42,18.5 , 1.0, 95)
midi.addNote(0, 9, 38,19 , 1.0, 90)
midi.addNote(0, 9, 42,19 , 1.0, 95)
midi.addNote(0, 9, 42,19.5 , 1.0, 95)
midi.addNote(0, 9, 42,20 , 1.0, 90)
midi.addNote(0, 9, 36,20 , 1.0, 90)
midi.addNote(0, 9, 42,20.5 , 1.0, 90)
midi.addNote(0, 9, 38,21 , 1.0, 90)
midi.addNote(0, 9, 42,21 , 1.0, 90)
midi.addNote(0, 9, 42,21.5 , 1.0, 90)
midi.addNote(0, 9, 36,22 , 1.0, 95)
midi.addNote(0, 9, 42,22 , 1.0, 95)
midi.addNote(0, 9, 42,22.5 , 1.0, 95)
midi.addNote(0, 9, 38,23 , 1.0, 90)
midi.addNote(0, 9, 42,23 , 1.0, 95)
midi.addNote(0, 9, 42,23.5 , 1.0, 95)
midi.addNote(0, 9, 42,24 , 1.0, 90)
midi.addNote(0, 9, 36,24 , 1.0, 90)
midi.addNote(0, 9, 42,24.5 , 1.0, 90)
midi.addNote(0, 9, 38,25 , 1.0, 90)
midi.addNote(0, 9, 42,25 , 1.0, 90)
midi.addNote(0, 9, 42,25.5 , 1.0, 90)
midi.addNote(0, 9, 36,26 , 1.0, 95)
midi.addNote(0, 9, 42,26 , 1.0, 95)
midi.addNote(0, 9, 42,26.5 , 1.0, 95)
midi.addNote(0, 9, 38,27 , 1.0, 90)
midi.addNote(0, 9, 42,27 , 1.0, 95)
midi.addNote(0, 9, 42,27.5 , 1.0, 95)
midi.addNote(0, 9, 42,28 , 1.0, 90)
midi.addNote(0, 9, 36,28 , 1.0, 90)
midi.addNote(0, 9, 42,28.5 , 1.0, 90)
midi.addNote(0, 9, 38,29 , 1.0, 90)
midi.addNote(0, 9, 42,29 , 1.0, 90)
midi.addNote(0, 9, 42,29.5 , 1.0, 90)
midi.addNote(0, 9, 36,30 , 1.0, 95)
midi.addNote(0, 9, 42,30 , 1.0, 95)
midi.addNote(0, 9, 42,30.5 , 1.0, 95)
midi.addNote(0, 9, 38,31 , 1.0, 90)
midi.addNote(0, 9, 42,31 , 1.0, 95)
midi.addNote(0, 9, 42,31.5 , 1.0, 95)
midi.addTempo(1, 0, 118)
time_signature = ( 4 ,  4 )
midi.addTimeSignature(1, 0, *time_signature, 24)
midi.addProgramChange(1, 0, 0, 32)
midi.addNote(1, 0, 42,12 , 1.0, 90)
midi.addNote(1, 0, 38,12.5 , 1.0, 90)
midi.addNote(1, 0, 40,13 , 1.0, 90)
midi.addNote(1, 0, 37,13.5 , 1.0, 90)
midi.addNote(1, 0, 38,14 , 1.0, 90)
midi.addNote(1, 0, 42,14.5 , 1.0, 90)
midi.addNote(1, 0, 45,15 , 1.0, 95)
midi.addNote(1, 0, 40,15.5 , 1.0, 95)
midi.addNote(1, 0, 42,16 , 1.0, 90)
midi.addNote(1, 0, 38,16.5 , 1.0, 90)
midi.addNote(1, 0, 40,17 , 1.0, 90)
midi.addNote(1, 0, 37,17.5 , 1.0, 90)
midi.addNote(1, 0, 38,18 , 1.0, 90)
midi.addNote(1, 0, 42,18.5 , 1.0, 90)
midi.addNote(1, 0, 45,19 , 1.0, 95)
midi.addNote(1, 0, 40,19.5 , 1.0, 95)
midi.addNote(1, 0, 42,20 , 1.0, 90)
midi.addNote(1, 0, 38,20.5 , 1.0, 90)
midi.addNote(1, 0, 40,21 , 1.0, 90)
midi.addNote(1, 0, 37,21.5 , 1.0, 90)
midi.addNote(1, 0, 38,22 , 1.0, 90)
midi.addNote(1, 0, 42,22.5 , 1.0, 90)
midi.addNote(1, 0, 45,23 , 1.0, 95)
midi.addNote(1, 0, 40,23.5 , 1.0, 95)
midi.addNote(1, 0, 42,24 , 1.0, 90)
midi.addNote(1, 0, 38,24.5 , 1.0, 90)
midi.addNote(1, 0, 40,25 , 1.0, 90)
midi.addNote(1, 0, 37,25.5 , 1.0, 90)
midi.addNote(1, 0, 38,26 , 1.0, 90)
midi.addNote(1, 0, 42,26.5 , 1.0, 90)
midi.addNote(1, 0, 45,27 , 1.0, 95)
midi.addNote(1, 0, 40,27.5 , 1.0, 95)
with open("./output/billiejean.mid", "wb") as output_file:
   midi.writeFile(output_file)
