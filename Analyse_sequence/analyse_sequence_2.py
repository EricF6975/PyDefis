print("----- Analyse sequence 2/2 ---------")

dict1={'A':'A','C':'C','G':'G','U':'U','R':'AG','Y':'CU','K':'GU','M':'AC','S':'CG','W':'AU','B':'CGU','D':'AGU',
       'H':'ACU','V':'ACG','N':'ACGU'}

def test_sequence(seq_init, sequence):
    #print(f"sequence initiale:{seq_init}, sequence à tester:{sequence}")

    test_caract=True
    pos_caract=0
   
    #print(f"longueur chaine : {len(sequence)}")
    while pos_caract<len(sequence) and test_caract==True:
        #print(f"{pos_caract} / {seq_init[pos_caract]} / {dict1[seq_init[pos_caract]]} /  {sequence[pos_caract]}")
       # print(dict1[seq_init[i]}])
        if sequence[pos_caract] not in dict1[seq_init[pos_caract]]:
            test_caract=False
            print(f"sequence : {sequence} caractere : {sequence[pos_caract]} position {pos_caract}")
        pos_caract+=1
    
    #print(test_caract)
    return test_caract
    

sequence_initiale=''
cnt_ok=0

with open('C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Analyse_sequence_2\\Sequence_2.txt','r') as file:
    i=0
    for line in file:
        line=line.rstrip("\n")
        if i==0:
            sequence_initiale=line
            print(f"sequence initiale:{sequence_initiale}")
        elif i>1:
            #print(line)
            if test_sequence(sequence_initiale,line):
                cnt_ok+=1
        i+=1

print(f"Resultat:{cnt_ok}")

#MNGHNNNNNKRRBNN
#CGGAAAGCGGGUGUU
