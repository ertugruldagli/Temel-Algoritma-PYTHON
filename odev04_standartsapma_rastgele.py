import random
import math

k=[]
toplam=0
farktop=0
for i in range(10000):
    k.append(random.randint(0,100))
    toplam+=k[i]

print("toplamı:", toplam)
o=toplam/len(k)
print("Ortalaması:", o)

for toplam in k:
    f=toplam-o
    f**=2
    farktop+=f
s=math.sqrt(farktop)


print("s.sapması:",s)

