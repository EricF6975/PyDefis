mot="fourchette"
print(mot)
print(len(mot))

for i in range(0,len(mot)):
    print(mot[i])

print("------------------")
mot_filtre=filter(lambda x : x>'j', mot )
print(type(mot_filtre))
print(list(mot_filtre))

liste_carac = list(map(lambda x, x, mot))