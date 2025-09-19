print("--- Desamorcage Tony Stark v2 -----")

nb_max=1435
 
def test_mult35(x):
    if x%3==0:
        return True
    if x%5==0:
        return True
    
som=0
for n in range(0,nb_max):
    if test_mult35(n):
        som+=n

    #print(f"n:{n} / som:{som}")

print(f"code = {som}")