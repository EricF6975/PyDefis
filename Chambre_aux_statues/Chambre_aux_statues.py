"""
_ rg1 : Si valeur = 3 alors la 1ere statue est forcément petite (taille 0)
_ rg2 : Si valeur = 3 et opposée=2 : alors les 3 1eres sont forcément taille 0,1,2, la derniere est 0 ou 1
_ rg3 Si valeur = 3 et opposée=1 alors la derniere est forcménent taille 2 
_rg4 : si val=1 et opposée=1 alors les 2 st egales et les positions 1 et 2 sont <=

_ ecrire procedure de test de cohrence une foisu que toutes les valeurs sont uniques
_procedure de brute force pour toutes les valeurs non uniques


"""

def affiche_salle(salle):
    for i in range(0,4):
        for j in range(0,4):
            print(f"{salle[i][j]} ", end="")
        print('\n')

def regles_3():
    print("-------  Amy -----")
    for i in range(0,4):
        print(amy[i])
        #print(f"i:{i} /  : {statues[i][0]}")
       
        if amy[i]==3:
            print(f" 3 tailles --> 1ere statue = 0 ")
            statues[i][0]='0'

            if clara[i]==2:
                statues[i][1]='1'
                statues[i][2]='2'
                statues[i][3]='01'
            else: #clara==1
                statues[i][3]='2'

    affiche_salle(statues)

    print(" ---- Clara -----")
    for i in range(0,4):
        print(clara[i])
        #print(f"i:{i} /  : {statues[i][0]}")
       
        if clara[i]==3:
            print(f" 3 tailles --> 1ere statue = 0 ")
            statues[i][3]='0'

            if amy[i]==2:
                statues[i][2]='1'
                statues[i][1]='2'
                statues[i][0]='01'
            else: #amy==1
                statues[i][0]='2'

    print("--------  Rose  ---------")
    for i in range(0,4):
        print(rose[i])
        #print(f"i:{i} /  : {statues[i][0]}")
       
        if rose[i]==3:
            print(f" 3 tailles --> 1ere statue = 0 ")
            statues[0][i]='0'

            if rory[i]==2:
                statues[1][i]='1'
                statues[2][i]='2'
                statues[3][i]='01'
            else: #rory==1
                statues[3][i]='2'

    print(" -----  rory ----------")
    for i in range(0,4):
        print(rory[i])
        #print(f"i:{i} /  : {statues[i][0]}")
       
        if rory[i]==3:
            print(f" 3 tailles --> 1ere statue = 0 ")
            statues[3][i]='0'

            if rose[i]==2:
                statues[2][i]='1'
                statues[1][i]='2'
                statues[0][i]='01'
            else: #rose==1
                statues[0][i]='2'


def regle_1(): # si une val==1 toutes les autres sont <=, donc on supprime les val sup
    print("--- regle des 1 --- ")
    for i in range(4):
        if amy[i]==1:
            for j in range(1,4):
                for n in range(0,len(statues[i][j])):
                    print(int(statues[i][j][n]))
                    if int(statues[i][j][n])>int(statues[i][0]):
                        statues[i][j][n]=''

    
def analyse_terminee():
    for i in range(4):
        for j in range(4):
            if len(statues[i][j])>1:
                return False
    return True

def test_amy(i): #ligne i
    print(f"---- Test amy ligne {i}---")
    cnt=1
    max='0'
    print(f"amy[{i}]={amy[i]}")
    for j in range(4):
        if len(statues[i][j])>1:
            return False
        elif statues[i][j]>max:
            max=statues[i][j]
            cnt+=1
    if cnt!=amy[i]:
        return False
    else:
        return True
        



        

# ---------------   MAIN ----------------
print("--- Chambre aux statues -----")

# ---  init_observations ------
observations=[3, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 3, 1, 2, 3]
amy=[]
rory=[]
clara=[]
rose=[]
for i in range(0,4):
    amy.append(observations[i])
    rory.append(observations[4+i])
    clara.append(observations[11-i])
    rose.append(observations[15-i])

print(f"amy:  {amy}")
print(f"clara:{clara}")

print(f"rose: {rose}")
print(f"rory: {rory}")

# ------- init statues -------------

statues=[['012' for i in range(4)] for j in range(4)]
print(statues)

affiche_salle(statues)
regles_3()
affiche_salle(statues)

regle_1()
affiche_salle(statues)

print(f"Analyse terminée = {analyse_terminee()}")

for i in range(4):
    print(test_amy(i))