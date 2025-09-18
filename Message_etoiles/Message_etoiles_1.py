from PIL import Image
import glob
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot

print("-----  Message des étoiles partie 1 --------")

def calc_coord(n):
     x=math.floor(n/800)
     y=n%800
     print(f"(x,y) : {x},{y}")
     return (x,y)

path='C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Message_des_étoiles\\telescope01\\*.png'

liste_toutes_img=[]

for file in glob.glob(path):
    #print(file)
    img=Image.open(file)
    #print(img.format, img.size, img.mode)
    pixel_value=list(img.getdata())

    print(len(pixel_value))
    pixel_sum=[]


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
            liste_h_etoiles.append(i)



list_coord_etoiles=[]
for i in range(0,len(liste_h_etoiles)):
     list_coord_etoiles.append(calc_coord(liste_h_etoiles[i]))


x=[]
y=[]
for i in range(len(list_coord_etoiles)):
     x.append(list_coord_etoiles[i][0])
     y.append(list_coord_etoiles[i][1])
     plt.scatter(x,y)
pyplot.show()
     
          