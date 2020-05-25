#After adding the library to python
#Install musescore and timidity
#  sudo apt-get install timidity
#  sudo apt-get install musescore
#Open python
#import music21
#music21.environment.set("musicxmlPath", "/usr/bin/musescore")
#music21.environment.set("midiPath", "/usr/bin/timidity")

#Documentation: https://web.mit.edu/music21/doc/
#to turn on timidity 
# timidity -iA &
# Now you can use timidity port in linthesia


from music21 import *
#s = corpus.parse('bach/bwv65.2.xml')
#s.show('midi')
#s.show()

f = note.Note("F5")
f.show('midi')