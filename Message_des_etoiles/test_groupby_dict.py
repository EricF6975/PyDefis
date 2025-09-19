from collections import defaultdict
from math import floor



def group_by(lst,fn):
    d = defaultdict(list)
    print(d)
    for el in lst:
        d[fn(el)].append(el)
    return dict(d)


liste_test= [1,2,5,1,4,3,6,5]
cnt = group_by(liste_test,floor)
print(cnt)

print(type(liste_test))
