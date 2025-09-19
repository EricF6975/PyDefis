# Enregistreur caché
import wave
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq

print("---- Enregisteur caché 2 -----")

# path="C:\\Users\\EFEUERSTEIN\\Documents\\Formations\\Python\\pyDefi\\Enregistreur_cache\\enregistrements_02\\"
# fich1='enregistrement_01.wav'
# fich2='enregistrement_03.wav'

path="C:\\Users\\EFEUERSTEIN\\Documents\\Formations\\Python\\pyDefi\\Enregistreur_cache\\"
fich1='enregistrement_01a.wav'
fich2='enregistrement_01b.wav'

fig, ax = plt.subplots()

liste_somme=[]


with wave.open(path+fich1,"rb") as wav_file1:
    #print(f"Nombre de canaux : {wav_file1.getnchannels()}")
    print(f"Taux d'échantillonnage : {wav_file1.getframerate()}")
    #print(f"Nombre de frames fich1: {wav_file1.getnframes()}")
    #frames_1 = wav_file1.readframes(wav_file1.getnframes())
    #frames_1 = wav_file1.readframes(10)
    #print(frames_1)
    #print(type(wav_file1))
    #print(type(wav_file1.readframes(1)))
    print(f"longueur : {len(wav_file1.readframes(1))}")
    print(f"conversion int: {int.from_bytes(wav_file1.readframes(1),"big",signed="True")}")
    print(wav_file1.readframes(10))
    print(wav_file1.tell())
    wav_file1.rewind()

    with wave.open(path+fich2,"rb") as wav_file2:
        print(f"Nombre de frames fich2: {wav_file2.getnframes()}")
        print(wav_file2.readframes(1))
        wav_file2.rewind()

    

  
        for i in range(wav_file1.getnframes()):
        #for i in range(2000):
            #print(f"i={i}")
            frame1_byte=wav_file1.readframes(1)
            frame2_byte=wav_file2.readframes(1)
            #print(f"frame1_byte={frame1_byte}  frame2_byte={frame2_byte}")

            frame1_int=int.from_bytes(frame1_byte,"big",signed="True")
            frame2_int=int.from_bytes(frame2_byte,"big",signed="True")
            somme_int=round((frame1_int+frame2_int)/2)
            #somme_int=frame1_int
            #print(f"somme_int={somme_int} frame1_int={frame1_int}  frame2_int={frame2_int}")


            liste_somme.append(somme_int)

        

        #print(liste_somme)
        serie_somme=pd.Series(liste_somme)
        ndarray_somme=np.ndarray(shape=(len(liste_somme)))

        for i in range(len(liste_somme)):
            ndarray_somme[i]=liste_somme[i]

        normalized_tone = np.int16((ndarray_somme / ndarray_somme.max()) * 32767)

        #print(serie_somme)
        #print(f"Moyenne = {serie_somme.mean()}")
        #print(f"Median = {serie_somme.median()}")
        #print(f"Pct_change = {serie_somme.pct_change()}")
        #print(f"Describe = {serie_somme.describe()}")

        print(type(normalized_tone))

        # Number of samples in normalized_tone
        SAMPLE_RATE=44100
        #DURATION=10
        N = len(liste_somme)

        yf = fft(normalized_tone)
        xf = fftfreq(N, 1 / SAMPLE_RATE)

        print(f"yf={type(yf)} / xf={type(xf)}")

        print(f"shape yf={yf.shape}")
        print(f"shape xf={xf.shape}")

        plt.plot(xf, np.abs(yf))
        plt.show()

        # The maximum frequency is half the sample rate
        points_per_freq = len(xf) / (SAMPLE_RATE / 2)

        # Our target frequency is 4000 Hz
        target_idx_min = int(points_per_freq * 100)
        target_idx_max = int(points_per_freq * 400)

        print(f"target_idx_min={target_idx_min}")

        for i in range(len(yf)) :
            if xf[i]<target_idx_min or xf[i]>target_idx_max:
                yf[i]=0

        plt.plot(xf, np.abs(yf))
        plt.show()
        


            
                    

        




   