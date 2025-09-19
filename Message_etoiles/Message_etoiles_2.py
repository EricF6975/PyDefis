from PIL import Image
import glob
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot
import os
import configparser

print("-----  Message des étoiles partie 2 --------")

# calcul des coordonnées x,y en fonction de la position dans la liste (chaque ligne a 800 positions)
def calc_coord(n):
     x=math.floor(n/800)
     y=n%800
     print(f"(x,y) : {x},{y}")
     return (x,y)

# Récupération du chemin d'acces des fichiers image dans le fichier de config
config=configparser.ConfigParser()
chemin_courant=os.getcwd()
chemin_fich_conf=chemin_courant+'\\fich_config.ini'
config.read(chemin_fich_conf)
path=config['chemin_acces']['chem_mess_etoiles']

path=path+'telescope02\\*.png'

liste_toutes_img=[]

# Lecture de tous les fichiers image
for file in glob.glob(path):
    #print(file)
    img=Image.open(file)
    #print(img.format, img.size, img.mode)
    pixel_value=list(img.getdata())

    print(len(pixel_value))
    #print(sum(pixel_value[639999]))
    pixel_sum=[]
    #pixel_sum[0]=sum(pixel_value[0])


    for i in range(0,len(pixel_value)):
         pixel_sum.append(sum(pixel_value[i]))



    liste_toutes_img.append(pixel_sum)

    

print(f"long liste toutes img {len(liste_toutes_img)}")


df = pd.DataFrame(liste_toutes_img)
print(type(df))
print(df.info())
#print(df.describe())


liste_h_etoiles=[]
for i in range(0,640000):

     if df[i].max() > df[i].min():
          cnt=0
          for x in range(0,len(df[i])):
               
               if df[i][x]==df[i].max():
                    cnt+=1   
                    #print(f"cnt:{cnt}") 
          if cnt==1:
               liste_h_etoiles.append(i)
            #print(calc_coord(i))


list_coord_etoiles=[]
for i in range(0,len(liste_h_etoiles)):
     #print(calc_coord(liste_h_etoiles[i]))
     list_coord_etoiles.append(calc_coord(liste_h_etoiles[i]))

#print(list_coord_etoiles)

x=[]
y=[]
for i in range(len(list_coord_etoiles)):
     x.append(list_coord_etoiles[i][0])
     y.append(list_coord_etoiles[i][1])
     plt.scatter(y,x)
pyplot.show()
     
          
