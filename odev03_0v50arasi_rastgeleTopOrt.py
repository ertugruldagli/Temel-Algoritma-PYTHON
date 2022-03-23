import random
from random import shuffle

k=[]
toplam=0

for i in range(10):
    k.append(random.randint(0,50))
    toplam+=k[i]

o=toplam/len(k)
print(k)
print("Toplamı:", toplam)
print("Ortalaması:", o)




#print(sum(k))
#o=sum(k)/(len(k))
#print("Ortlaması",o)
