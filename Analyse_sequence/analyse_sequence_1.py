print("----- Analyse sequence 1/2 ---------")

dict1={'A':'A','C':'C','G':'G','U':'U','R':'AG','Y':'CU','K':'GU','M':'AC','S':'CG','W':'AU','B':'CGU','D':'AGU',
       'H':'ACU','V':'ACG','N':'ACGU'}

def calcule_nbre_seq(sequence):
    print(f'calcule nbre sequence : {sequence}')
    nombre_sequences=1

    for i in sequence:
        #print(i)
        #print(len(dict1[i]))
        nombre_sequences*= len(dict1[i])
    print(nombre_sequences)
    return nombre_sequences


nbre_seq= calcule_nbre_seq('NDNKCNVNUGYWRGCNABGSNCRACGSHWNNCYBCSNVUAAGDCMNKNYNNBNCGUBHUNRANDGDMDRSYMGSNWHNDNCVCMAMCANWKYRKVMWMKC')
code_sequence=str(nbre_seq)
print(code_sequence)
code_sequence=code_sequence[-5:]
print(code_sequence)
