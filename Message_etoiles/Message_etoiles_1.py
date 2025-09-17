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
    #print(sum(pixel_value[639999]))
    pixel_sum=[]
    #pixel_sum[0]=sum(pixel_value[0])


    for i in range(0,len(pixel_value)):
         pixel_sum.append(sum(pixel_value[i]))
        #  if sum(pixel_value[i])>0:
        #       print(f"index:{i} : {sum(pixel_value[i])}")


    #print(f"somme pixel: {pixel_sum}")

    #liste_toutes_img.append(list(img.getdata()))
    liste_toutes_img.append(pixel_sum)

    

#print(len(liste_toutes_img[0]))
print(f"long liste toutes img {len(liste_toutes_img)}")

#print(f"somme:{sum()}")

#for i in range(0,len(liste_toutes_img[0])):

#test
# liste_toutes_img[10][10]=20
# liste_toutes_img[2][15]=47
# liste_toutes_img[12][1200]=47



df = pd.DataFrame(liste_toutes_img)
print(type(df))
print(df.info())
#print(df.describe())


#test
#df.loc[10,10]=20
#df.loc[2,12]=200

#liste_min=[]
#liste_max=[]
liste_h_etoiles=[]
for i in range(0,640000):
#for i in range(0,2000):
     #liste_max.appen(df[i].max())
     #liste_min.append(df[i].min())
     #print(f"max :{df[i].max()} / min:{df[i].min()}")
     if df[i].max() > df[i].min():
            liste_h_etoiles.append(i)
            #print(calc_coord(i))

#print(f"index des etoiles apparues: {liste_h_etoiles}")

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
     plt.scatter(x,y)
pyplot.show()
     
          