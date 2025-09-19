# Enregistreur caché
import wave

print("---- Enregistreur caché -----")

path="C:\\Users\\EFEUERSTEIN\\Documents\\Formations\\Python\\pyDefi\\Enregistreur_cache\\"
fich1='enregistrement_01a.wav'
fich2='enregistrement_01b.wav'


with wave.open(path+fich1,"rb") as wav_file1:
    print(f"Nombre de canaux : {wav_file1.getnchannels()}")
    print(f"Taux d'échantillonnage : {wav_file1.getframerate()}")
    print(f"Nombre de frames fich1: {wav_file1.getnframes()}")
    #frames_1 = wav_file1.readframes(wav_file1.getnframes())
    #frames_1 = wav_file1.readframes(10)
    #print(frames_1)
    print(type(wav_file1))
    print(type(wav_file1.readframes(1)))
    print(f"longueur : {len(wav_file1.readframes(1))}")
    print(f"conversion int: {int.from_bytes(wav_file1.readframes(1),"big",signed="True")}")
    print(wav_file1.readframes(10))
    print(wav_file1.tell())
    wav_file1.rewind()

    with wave.open(path+fich2,"rb") as wav_file2:
        print(f"Nombre de frames fich2: {wav_file2.getnframes()}")
        print(wav_file2.readframes(1))
        wav_file2.rewind()

  
        with wave.open(path+'fich3.wav','wb') as wav_file3:
            wav_file3.setparams(wav_file1.getparams())
            #wav_file3.writeframes(wav_file1.readframes(wav_file1.getnframes())+wav_file2.readframes(wav_file1.getnframes()))
            print(f"nb frames 3 : {wav_file3.getnframes()}")

            for i in range(wav_file1.getnframes()):
            #for i in range(30):
                #print(f"i={i}")
                frame1_byte=wav_file1.readframes(1)
                frame2_byte=wav_file2.readframes(1)
                #print(f"frame1_byte={frame1_byte}  frame2_byte={frame2_byte}")

                frame1_int=int.from_bytes(frame1_byte,"big",signed="True")
                frame2_int=int.from_bytes(frame2_byte,"big",signed="True")
                somme_int=round((frame1_int+frame2_int)/2)
                #print(f"somme_int={somme_int} frame1_int={frame1_int}  frame2_int={frame2_int}")

                try:
                    somme_byte=somme_int.to_bytes(2, byteorder="big", signed="True")
                    #print(f"somme_byte={somme_byte}")
                    wav_file3.writeframes(somme_byte)
                except OverflowError:
                    print("Erreur")
                    

            print(f"nb frames 3 : {wav_file3.getnframes()}")

        with wave.open(path+'fich3.wav','rb') as wav_file3_r:
            print(wav_file3_r.readframes(10))




   