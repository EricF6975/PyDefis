import pandas as pd
import math

print(" ----  Test dataframe groupby -----")

liste_v=[]
for i in range(0,10):
    liste_h=[]
    for y in range(0,20):
        liste_h.append(y)
    print(liste_h)
    liste_v.append(liste_h)
print("liste_v : ")
print(liste_v)

df = pd.DataFrame(liste_v)
print(df.info())

#df.groupby(by=None,axis=1, level=None)
print(type(df[10][7]))

df.loc[7,10]=20
df.loc[2,8]=200
df.loc[4,19]=125

#print(df[7][10])
print(df[10][7])

print(type(df[10][7]))


print(df)
print(df[19][1])

print(df[19].max())
print(df[19].min())

liste_max=[]
liste_min=[]

for i in range(0,20):
    liste_max.append(df[i].max())
    liste_min.append(df[i].min())

print(liste_max)
print(liste_min)

# for x in range(0,len(liste_v)):
#    print(df[x][1])


print("---- Maths -----")
i=10
print(i/800)
print(math.floor(i/800))
print(i%800)

for x in range(0,len(liste_h)):
    #print(df[x].max().count())
    #print(df[x].groupby())
    print(f"Nom colonne : {df.columns[x]} / {type(df.columns[x])}")
    print(f"group by : {df.groupby(df.columns[x])}")
    print(f"group by count() : {df.groupby(df.columns[x]).count()}")
    print(f"max colonne : {df[x].max()} ")
    print(f" max du group by  : {df.groupby(df[x]).max()}")
    print(f"count du max : {df.groupby(df[x]).count().max()}")

    dict1={}
    dict1={df.groupby(df[:][x]):df.groupby(df[:][x]).count()}

    #dict_sans_for = {n: n**2 for n in nombres if n%2==0}

print(f"dict1={dict1}")
print("-----------------")
# print(type(dict1[19]))
# print(type(dict1[19].values))
# print(type(dict1[19].keys))
# print(dict1[19].keys())






