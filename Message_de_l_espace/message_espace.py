import pandas as pd
import glob

print("-- Message de l'espace -----")
# lecture fichier 

def test_sequence(sequence):
    est_sequence_rare=True
    #print(f"test sequence : {sequence}")
    i=0
    while i <len(sequence)-4 and est_sequence_rare==True:
        test_seq=sequence[i:i+4]
        #print(f"test_seq {test_seq}")
        test_list=[]
        for n in test_seq:
            #print(n)
            if n not in test_list:
                test_list.append(n)
        #print(f"test_list:{test_list} / longueur : {len(test_list)}")
        if len(test_list)<4:
                est_sequence_rare=False
        i+=1
    #print(f"Resultat sequence rare = {est_sequence_rare}")
   
    return est_sequence_rare

      
def test_fichier(fichier, min, max):
    
    chemin=fichier
    #print(f"lecture chemin {chemin}")
    liste_resultat_fichier=[]
    cnt_line=0
    with open(chemin,'r') as file:
        #print(f"---- Lecture fichiers {file} -----")
        for line in file:
            cnt_line+=1
            #print(line)
            #print(test_sequence(line))
            liste_resultat_fichier.append(test_sequence(line))
    #print(liste_resultat_fichier)

    #comptage des sequences rares
    #cnt_seq_rare=0
    cnt_seq_rare=sum(map(lambda x:1 if x==True else 0, liste_resultat_fichier))
    #print(f"cnt_seq_rare : {cnt_seq_rare}")

    if cnt_seq_rare<min or cnt_seq_rare>max:
         return True
    else:
         return False



#------------  main -----------
#path='C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Message_de_l_espace\\'
#path='C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Message_de_l_espace\\rep_test\\*'
path='C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Message_de_l_espace\\radio_enregistrements\\*'
liste_resultats_tous_fichiers=[]
min=172
max=235
for file in glob.glob(path):
     #print(f"fichier : {file}")
     #print(f"path : {path}")
     num_fichier=int(file[len(path)+4:-4])
     #print(f"num_fichier:{num_fichier}")
     liste_resultats_tous_fichiers.append((num_fichier, test_fichier(file,min,max)))

print(liste_resultats_tous_fichiers)

for result in liste_resultats_tous_fichiers:
     if result[1]==True:
          print(str(result[0])+", ", end="")

     
     



