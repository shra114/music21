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
'''
typeFromNumDict = {
    1.0: 'whole',
    2.0: 'half',
    4.0: 'quarter',
    8.0: 'eighth',
    16.0: '16th',
    32.0: '32nd',
    64.0: '64th',
    128.0: '128th',
    256.0: '256th',
    512.0: '512th',
    1024.0: '1024th',
    2048.0: '2048th',
    0.0: 'zero',
    0.5: 'breve',
    0.25: 'longa',
    0.125: 'maxima',
    0.0625: 'duplex-maxima',
    }
'''
def gen_stream(list1):
    stream1 = stream.Stream()
    for i in list1:
        if (isinstance(i,list)):
            d = duration.Duration()
            d.quarterLength  = i[1]
            note1 =note.Note(i[0])
            note1.duration.type = d.type
            stream1.append(note1)
        else:
            stream1.append(note.Note(i))
    return stream1
def show_stream(list1):
    gen_stream(list1).show()

def play_stream(list1):
    gen_stream(list1).show('midi')

#cmajor_scale =["C","D","E","F","G","A","B","C5"]
#play_stream(cmajor_scale)
#show_stream(cmajor_scale)

sample_stream = [["C",2], "D","E"] #C 2 beats, D,E 1beat each
#show_stream(sample_stream)
#play_stream(sample_stream)

#happybirthday_stream = ["C","C",["D",2],["C",2], ["F",2], ["E",2]]
happybirthday_stream = [["C",0.5],["C",0.5],["D",1],["C",1], ["F",1], ["E",1]]
play_stream(happybirthday_stream)
