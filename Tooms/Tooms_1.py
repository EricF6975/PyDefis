# ----- TOOMS 1/2 -----------
import glob
import pandas as pd

print("----  TOOMS 1/2--------")
pth="C:/Users"
path="C:/Users/EFEUERSTEIN/Documents/Formations/Python/pyDefi/Tooms/"
files = glob.glob(path+'/*')
print(files)

fich_profil=open(path+'profil','r')
print(type(fich_profil))

df_profil = pd.read_csv(path+"profil", header=None, sep=",")
print(df_profil.head(5))
print(df_profil.shape)
print(type(df_profil))

profil_tooms=[10, 12, 6, 9, 18.5, 22, 7, 4, 9, 10]

for i in range(len(df_profil)):
    print(df_profil.iloc[i,0])

df_profil.insert(0,'idx','xxx')

#---- Formatage dataframe ----
for i in range(len(df_profil)):
    df_profil.iloc[i,0]=df_profil.iloc[i,1].split('-')[0].strip()
    df_profil.iloc[i,1]=df_profil.iloc[i,1].split('-')[1].strip()

print(df_profil.head(5))

total=0
# --- traitement dataframe -----
for i in range(len(df_profil)):
    print(f"Ligne {i} / index={df_profil.iloc[i,0]}")
    diff_prof_prec=float(df_profil.iloc[i,1])-float(profil_tooms[0])
    diff_prof=0
    for j in range(0,len(profil_tooms)):
        print(f"{df_profil.iloc[i,j+1]} - {str(profil_tooms[j])} = {float(df_profil.iloc[i,j+1])-float(profil_tooms[j])}")
        diff_prof=float(df_profil.iloc[i,j+1])-float(profil_tooms[j])
        if diff_prof!=diff_prof_prec:
            print('prof differentes / KO')
            break
        diff_prof_prec=diff_prof
    print(f"j={j}")

    if j==9:
        print(f" --------- profil OK  --------- ")
        total+=int(df_profil.iloc[i,0])
        print(f"Total={total}")

    print(f"Fin traitement, total={total}")







      