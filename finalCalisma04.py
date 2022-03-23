#map - filter - reduce

#map: dizi elemanlarının tamamına uygulanacak işlemlerde kullanılır.

liste=[2,5,6,7,9]
yl= list(map(lambda x:x**2,liste))
print(yl)

def ikikat(x):
    return x*2
def yari(x):
    return x/2
fonk=[ikikat,yari]
for i in range(5):
    deger= list(map(lambda x:x(i),fonk))
    print(deger)

#filter: dizi elemlarının filtrelenmesinde kullanılabilir.

l=[1,9,6,8,7,3,4,5,0]
#uckati=list(map(lambda x: x%3==0,l))
uckati=list(filter(lambda x: x%3==0,l))
print(uckati)

#reduce: dizi elemanlarının toplanması veya çarpılması gibi işlemlerde kullanılır.

from functools import reduce
toplam= reduce(lambda x,y:x+y,l)
carp= reduce(lambda x,y:x*y,l)
print(toplam)
print(carp)

