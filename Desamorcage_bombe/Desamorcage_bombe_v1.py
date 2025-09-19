print("----  Desamorcage bombe v1------")



def calc_num(x):
    num=str(x*13)
    print(type(num))
    print(num)
    print(num[-3:])
    return int(num[-3:])

num_serie='797114'
u=int(num_serie[0:3])
n=int(num_serie[3:6])
print(f"num_serie: {num_serie} / u:{u} / n: {n}")

for i in range(0,n):
    u = calc_num(u)

print(f"numero fil = {u}")

