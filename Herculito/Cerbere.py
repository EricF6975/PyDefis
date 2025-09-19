
# Herculito XII
import math
print("------  Herculito XII -------")

distance=13979
dist_carre=distance**2
print(dist_carre)

resultats=[]

for ouest in range(1,distance):
    #print(f"ouest:{ouest} / ouest carre:{ouest**2}")
    nord_carre = dist_carre - ouest**2
    nord = math.sqrt(nord_carre)
    #print(f"nord carre:{nord_carre} / nord:{nord}")
    if math.floor(nord)==nord:
        #print("ok")
        resultats.append((ouest,int(nord)))

print(resultats)
print(sorted(resultats))

#liste_test=[1,6,9,454,1,4]
#liste_test.sort()
#print(liste_test)
