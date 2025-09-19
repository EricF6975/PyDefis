print("----- Desamorcage Tony Stark ------")
som3=0
som5=0
nb_max=20

mult3=0
mult5=0
i=0

while 3*i<nb_max:
    mult3=3*i
    som3+=mult3
    print(f"i={i} / mult3={mult3} / som3={som3}")
    i+=1

i=0
while 5*i<nb_max:
    mult5=5*i
    som5+=mult5
    print(f"i={i} / mult5={mult5} / som5={som5}")
    i+=1

code = som5+som3
print(code)

print(3 + 5 + 6 + 9 + 10 + 12 + 15 + 18)
print(3 + 6 + 9 + 12 + 15 + 18)