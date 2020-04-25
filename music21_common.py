from music21 import *

def play_note(mynote):
    f = note.Note(mynote)
    f.show('midi')
def show_note(mynote):
    f = note.Note(mynote)
    f.show()

#play_note("C")
#play_note("D")
#play_note("E")

def show_stream(list1):
    stream1 = stream.Stream()
    for i in list1:
        stream1.append(note.Note(i))
    stream1.show()

def play_stream(list1):
    stream1 = stream.Stream()
    for i in list1:
        stream1.append(note.Note(i))
    stream1.show('midi')

cmajor_scale =["C","D","E","F","G","A","B","C5"]
play_stream(cmajor_scale)
show_stream(cmajor_scale)

