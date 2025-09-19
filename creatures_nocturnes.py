#----- creatures nocturnes ------
print("---------  creatures nocturnes -------")

seconde_courante=0
nouvelles_chauve_souris=10
nouveaux_skellingtons=5
nouveaux_zombies=4
nouveaux_fantomes=3

tue_chauve_souris=2
tue_skellingtons=1
tue_zombie=1
tue_fantome=1

creatures=[0,0,0,0] # chauve-souris / skellingtons / zombies / fantomes

while seconde_courante < 50*60:
    seconde_courante+=1

    if seconde_courante%2==0:
        creatures[0]+=nouvelles_chauve_souris
    if seconde_courante%5==0:
        creatures[1]+=nouveaux_skellingtons
    if seconde_courante%6==0:
        creatures[0]-=tue_chauve_souris
        creatures[2]+=nouveaux_zombies
    if seconde_courante%10==0:
        creatures[3]+=nouveaux_fantomes
    if seconde_courante%20==0:
        creatures[1]-=tue_skellingtons
    if seconde_courante%30==0:
        creatures[2]-=tue_zombie
    if seconde_courante%40==0:
        creatures[3]-=tue_fantome
    if seconde_courante%240==0:
        tue_chauve_souris+=2
        tue_skellingtons+=1
        tue_zombie+=1
        tue_fantome+=1

    print(f"temps : {seconde_courante} / creatures : {creatures}")
