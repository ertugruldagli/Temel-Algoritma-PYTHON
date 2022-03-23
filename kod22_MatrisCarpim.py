import random

m1 = [[random.randint(0,4) for i in range(3)] for j in range(3)]
m2 = [[random.randint(0,4) for i in range(3)] for j in range(3)]
mc = [[0 for i in range(3)] for j in range(3)]
print(m1)
print(m2)
#print(mc)

toplam = 0

for i in range(3):
    for j in range(3):
        toplam = 0
        for k in range(3):
            toplam += m1[i][k]*m2[k][j]
        mc[i][j]=toplam

print(mc)