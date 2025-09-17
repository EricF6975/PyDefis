print("-------  Herculito XI Le jardin des Hespérides ---------")

total=0

for i in range(1,51):
    print(i)
    carre=i*i
    print(carre)
    print(carre%3)

    if round(carre%3)==0:
        total+=carre
        print(f"total: {total}")

print(f"Total pommes = {total}")
