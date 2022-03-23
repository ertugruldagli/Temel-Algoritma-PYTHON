import random

d1=[]
d2=[]
for i in range(100000):
    d1.append(random.randint(0,1332))
    for j in d1:
     if j>600 or j<700:
        d2.append(j)
        print(d2)

