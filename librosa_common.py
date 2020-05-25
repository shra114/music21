import  librosa
import librosa.display
import matplotlib.pyplot as plt

#y, sr = librosa.load(librosa.util.example_audio_file())
#y, sr = librosa.load('/home/shra1/Documents/MuseScore3/Scores/Let_it_be_book_version.wav')
y, sr = librosa.load('/home/shra1/Documents/MuseScore3/Scores/sample.wav')

#y, sr = librosa.load('download.wav')
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
C = librosa.cqt(y,sr)
chroma = librosa.feature.chroma_cqt(C=C,sr=sr)
plt.subplot(3,1,1)
librosa.display.specshow(chroma,x_axis='time',y_axis='chroma')
plt.subplot(3,1,2)
librosa.display.specshow(chroma,x_axis='time',y_axis='chroma')
plt.subplot(3,1,3)
librosa.display.waveplot(y[0:10])
plt.show()





#print (sr)
#print (len(pitches))
#for i in pitches:
#    print (i)
#    print (len(i))
#    break
##all_notes = []
##all_magnitudes = []
##plt.figure()
###librosa.display.waveplot(y, sr=sr)
##plt.title('This wave')
##for i in pitches:
##    for k in i:
##        all_notes.append(float(k))
#
#for i in magnitudes:
#    for k in i:
#        all_magnitudes.append(float(k))
#
#count = 0
#print (len(all_notes), len(all_magnitudes))

#ln = len(all_notes)
#interval = int(ln/100)
#max_mag  =  (max(all_magnitudes))
#for k in all_notes[::interval]:
#    count +=1
#    magnitude = all_magnitudes[all_notes.index(k)]
#    if((k!=0.0) and (magnitude > 0.9*max_mag)) :
#        note='Yes'
#    else:
#        note="No"
#    #print(count, k, all_notes.index(k), note, magnitude)
#
##plt.plot(all_notes)
##plt.show()
