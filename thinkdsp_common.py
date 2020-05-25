import thinkdsp

violin = thinkdsp.read_wave('download.wav')
violin.make_audio()
spectrogram = violin.make_spectrogram(seg_length=1024)
spectrogram.plot(high=5000)
