#rastgele sayılarla doldurulmuş iki matrisi toplayalım
import random

m1=[[0 for x in range(3)]for y in range(3)]
m2=[[0 for x in range(3)]for y in range(3)]
mt=[[0 for x in range(3)]for y in range(3)]

for i in range(3):
    for j in range(3):
        m1[i][j]=random.randint(0,4)
        m2[i][j] = random.randint(0, 4)
        mt[i][j]=m1[i][j]+m2[i][j]
print(m1)
print(m2)
print(mt)

print("m1 matrisi")
for i in range(3):
    print(m1[i])