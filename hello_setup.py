#After adding the library to python
#Install musescore and timidity
#Open python
#import music21
#music21.environment.set("musicxmlPath", "/usr/bin/musescore")
#music21.environment.set("midiPath", "/usr/bin/timidity")

from music21 import *
s = corpus.parse('bach/bwv65.2.xml')
s.show('midi')
s.show()
