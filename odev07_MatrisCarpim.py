import random

m1=[[0 for x in range(2)]for y in range(2)]
m2=[[0 for x in range(2)]for y in range(2)]
mc=[[0 for x in range(2)]for y in range(2)]

for i in range(2):
    for j in range(2):
        m1[i][j]=random.randint(1,5)
        m2[i][j]=random.randint(1,5)
        mc[i][j]+= m1[i][j]* m2[i][j]

print("m1 matrisi")
for i in range(2):
    print(m1[i])

print("m2 matrisi")
for i in range(2):
    print(m2[i])

print("carpimları")
for i in range(2):
 print(mc[i])