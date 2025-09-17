print(" ----- Herculito I : Le lion de Némée ---------")

def calc_num_divinite(divinite):
    num_lettre=0
    somme_lettre=0
    for n in divinite:
        num_lettre=ord(n)-64
        somme_lettre+=num_lettre
        #print(f"n:{n} / num_lettre: {num_lettre} / somme={somme_lettre}")
    return somme_lettre

chaine_noms='ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS ERIS EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO MAIA METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE SELENE THEMIS THETIS TRITON ZEUS'
liste_noms=chaine_noms.split()
print(liste_noms)
dict1={}

dict1 = {divinite:calc_num_divinite(divinite) for divinite in liste_noms}

print(dict1)

print("----- Tri ------")
sorted_divinites=dict(sorted(dict1.items(),key=lambda item:item[1]))
print(sorted_divinites)
print(" ---- liste tri noms ----")
print(sorted_divinites.keys())

print("--------------")
for divi in sorted_divinites.keys():
    print(divi+" ", end="")
