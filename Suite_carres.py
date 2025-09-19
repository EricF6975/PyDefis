print(" ---- Py Defi --  Suite carré ----")

def calcule_somme_carres(nbre):
    nbre_str=str(nbre)
    #print(nbre_str)
    somme=0
    for i in range(0,len(nbre_str)):
        #print(nbre_str[i])
        somme+=int(nbre_str[i])**2

    return somme

def calcule_suite(nbre):
    nb_courant=nbre
    resultats=[nb_courant]
    cnt=0
    somme=0
    while (cnt<200 and somme!=4):
        #print(f"nb_courant:{nb_courant}")
        cnt+=1
        #print(cnt)
        somme=calcule_somme_carres(nb_courant)
        #print(f"somme carrés:{somme}")
        resultats.append(somme)
        nb_courant=somme
    #print(f"Resultats:{resultats}")
    print(type(resultats))

    if somme==4:
        print("4 trouvé")
        return True
    else:
        print("4 pas trouvé")
        return False

liste_resultats=[]
#print(type(liste_resultats))

for i in range(1,101):
    liste_resultats.append(calcule_suite(i))

print(f"Resultats:{liste_resultats}")
print(f"Nbre de cas : {liste_resultats.count(True)}")