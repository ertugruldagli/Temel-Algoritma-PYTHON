import random


d=[]
def ras(d):

    for s in range(100):
        i = random.randint(0, 10)
        d.append(i)
    return d
print(ras(d))