#anonim ve lambda fonksiyonlar

def topla(a,b):
    return a+b

k = lambda x,y:x*y
print(k(3,4))

dizi = [3,2,0,2,5,7,8,4,9]
print(dizi)

cift = list(filter(lambda x:x%2==0,dizi))
print(cift)

tek = list(filter(lambda x:x%2==1,dizi))
print(tek)

print(topla(5,6))