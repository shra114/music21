from music21 import *

def play_note(mynote):
    f = note.Note(mynote)
    f.show('midi')
def show_note(mynote):
    f = note.Note(mynote)
    f.show()

play_note("C")
play_note("D")
play_note("E")

