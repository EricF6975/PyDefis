import string

print(" --------------------  Meli-Melo d'adresses  -------------")
code_a_trouver='1a6e1g1i1l1m1n1o2r2s2u1y'

def test_lettre(caractere):
    return caractere.isalpha()

#-----------------------------------------------
def calcule_empreinte(phrase):
    #print(f"calcule empreinte : {phrase}")
    phrase=list(filter(test_lettre,phrase))
    #print(phrase)
    dict1={k:phrase.count(k) for k in phrase}
    #print(type(dict1))
    lst=list(dict1.keys())
    lst.sort()
    #print(lst)
    code=''
    for i in lst:
        code +=str(dict1[i])+i
    #print(code)
    return code

#----------------------------------------------
with open('C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Meli_Melo_adresses\\C24_adresses.txt','r') as file:
    for line in file:
        #print(line)
        empreinte = calcule_empreinte(line)
        #print(empreinte)
        if empreinte==code_a_trouver:
            print(f"adresse trouvée: {line}")







