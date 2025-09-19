print("---- desamorcage_bombe_cdUp19 -------")

def permute_code(code, permutation):
    #print(type(code))
    code_lst=list(code)
    i=int(permutation[0])-1
    j=int(permutation[1])-1
    #print(f"i={i} / j={j} / code[i]:{code_lst[i]}")
    code_lst[i], code_lst[j] = code_lst[j],code_lst[i]
    print(f"code:{code_lst}")
    return ''.join(code_lst)


code_init='34125'

with open('C:\\Users\\EFEUERSTEIN\\Documents\\Formations\\Python\\pyDefi\\Desamorcage_bombe\\permutations.txt') as file:
    liste_perm=list(file)
    print(liste_perm)
    liste_perm=str(liste_perm[0]).split(", ")
    print(liste_perm)

    for perm in liste_perm:
        print(perm)
        code_init=permute_code(code_init,perm)
        print(code_init)