import requests
from defisurl import DefisUrl
print(" ---- Ballade sur un échiquier -------")

liste_mouv=[(0,1),(1,0),(0,-1),(-1,0)]
nb_case=0

print(f"liste_mouv:{liste_mouv}")

def tourne(index_mv,sens_rotation):
    #print(f"--------  Tourne:{sens_rotation} ------------")
    if sens_rotation=='D':
        index_mv=(index_mouv+1)%4
    elif sens_rotation=='G':
        if index_mv==0:
            index_mv=3
        else:
            index_mv-=1
    elif sens_rotation=='A':
        pass
        #print('pas de rotation')
    else:
        pass
        #print('Erreur rotation')

    #print(f"index_rotation:{index_mv} / prochain mouv: {liste_mouv[index_mv]}")

    return index_mv

def avance(pos, index_mv):
    x_nv_pos, y_nv_pos = pos[0]+liste_mouv[index_mv][0], pos[1]+liste_mouv[index_mouv][1]
    #print(f"Avance/ Nouvelle pos:{x_nv_pos},{y_nv_pos}")
    if x_nv_pos<1 or x_nv_pos>8 or y_nv_pos<1 or y_nv_pos>8:
        print("Erreur, sortie de l'échiquier")
        raise Exception(f"Erreur, sortie de l'échiquier")
    return (x_nv_pos, y_nv_pos)


d= DefisUrl('https://pydefis.callicode.fr/defis/BaladeEchiquier/get/EricF6975/0f0e4', verify=True)
lignes=d.get()

print("\n".join(lignes))

ordres=str(lignes)[2:-2]
#ordres='DAAAAAADDAADAADAAADAAGGAAGAAAADAAAA'
#ordres='DAA'
print(f"ordres={ordres}")
# mouv = direction du prochain mouv : 1er chiffre = mouv horizontal, 2e chiffre = mouv vertical
index_mouv=0
# pos : 1er chiffre = pos horizontale, 2e chiffre = pos verticale
pos=(1,1)
liste_cases=[pos]

for ordr in ordres:
    #print(f"Pos: {pos} / Ordre = {ordr}")
    index_mouv=tourne(index_mouv,ordr)
    if ordr=='A':
        pos=avance(pos,index_mouv)
    
    if pos not in liste_cases:
        liste_cases.append(pos)

num_cases='ABCDEFGH'
#print(f"nb_case:{len(liste_cases)}")
resultat=str(len(liste_cases))+str(num_cases[pos[0]-1])+str(pos[1])
print(f"resultat= {resultat}")
# url_reponse='https://pydefis.callicode.fr/defis/BaladeEchiquier/post/EricF6975/0f0e4'
# reponse_post = requests.post(url_reponse,data=resultat)
# print(reponse_post.status_code)

reponse_post=d.post(resultat)
# print(reponse_post)

