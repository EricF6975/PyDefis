import requests
import json

print("---- Ocean liquide Mimas ----")

r= requests.get('https://pydefis.callicode.fr/defis/C24_Mimas/get/EricF6975/e4002', verify=True)
print(r)
data=r.json()
print(data)

dict_resultats={} # dictionnaire des resultats toutes cartes
num_trou=0

for carte in data:
    print(f"---- {carte}------")
    num_trou+=1
    print(f"num_trou:{num_trou}")

    #def traite_carte(carte_courante):
    resultat=(10000,0,0) # resultat pour une carte = (valeur moy mini, n° ligne, n° colonne)

    #print(data['carte01'])
    #carte_courante=data['carte01']
    carte_courante=data[carte]


    print("------ ligne par ligne ------")
    for index, ligne in enumerate(carte_courante):
        #print(f"index : {index} / ligne: {ligne}")
        if index==0 or index==len(carte_courante)-1:
            #print("pas de calcul sur cette ligne")
            pass
        else:
            #print("calcul en cours")
            ligne_precedente=carte_courante[index-1]
            ligne_suivante=carte_courante[index+1]
            for i in range(1,len(ligne)-1):
                moy=0
                #print(f"i:{i} / valeurs : {ligne_precedente[i-1]} / {ligne_precedente[i]} / {ligne_precedente[i+1]} / {ligne[i-1]} / {ligne[i]} / {ligne[i+1]} / {ligne_suivante[i-1]} / {ligne_suivante[i]} / {ligne_suivante[i+1]} ")
                moy=(ligne_precedente[i-1]+ligne_precedente[i]+ligne_precedente[i+1]+ligne[i-1]+ligne[i]+ligne[i+1]+ligne_suivante[i-1]+ligne_suivante[i]+ligne_suivante[i+1])/9
                #print(f"moyenne:{moy} / mini:{resultat[0]}")
                if moy<resultat[0]:
                    resultat=(moy,index,i)
    
    print(f"num_trou:{num_trou}")
    dict_resultats['trou'+"{:02d}".format(num_trou)]=(resultat[1],resultat[2])
del dict_resultats["trou11"]
del dict_resultats["trou12"]
dict_resultats["signature"]=data['signature']
print(dict_resultats)


json_resultats=json.dumps(dict_resultats)
print(" ---JSON : ----")
print(json_resultats)


r = requests.post("https://pydefis.callicode.fr/defis/C24_Mimas/post/EricF6975/e4002", json=dict_resultats, verify=True)
print(r) # Pour contrôle
data = r.json()
print(data) # Pour contrôle
