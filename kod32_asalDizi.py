# 0-1000 arasındaki asal sayılardan oluşan
# 10 elemanlı dizi

import random

def asalmi(s):
    bolensayac = 0
    for i in range(2, s):

        if s % i == 0:
            bolensayac += 1

    if bolensayac > 0:
        return False
    else:
        return True
dizi=[]
sayac=0

while True:
    s=random.randint(0,1000)
    if asalmi(s):
        dizi.append(s)
        sayac+=1
        if sayac==10:
            break
print(dizi)