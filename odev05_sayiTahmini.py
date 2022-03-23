import random
s=random.randint(0,100)
#print(s)
t=int(input("bir sayi tahmin ediniz:"))
ts=0
while True:
    ts+=1
    if s==t:
        print("TEBRİKLER!!! Doğru tahmin")
        break
    elif t>s:
        t = int(input("Aşağı!! = "))
    else:
        t = int(input("Yukarı!! = "))

print("tahmin sayisi:",ts)




