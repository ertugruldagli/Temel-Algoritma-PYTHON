def ilk_fonksiyon():
    print("bu bizim ilk fonksiyonumuz..")
ilk_fonksiyon()

def merhaba(isim):
    print("Merhaba",isim)
merhaba("dunya")

def topla(a,b):
    return a+b
print(topla(3,6))


def fak(x):
    if x==1 or x==0:
        return 1
    else:
        return x * fak(x-1)
print(fak(0))



def top(dizi):
    if len(dizi) == 1:
        return dizi[0]
    else:
        return dizi[0]+ top(dizi[1:])
dizi=[5,6,3,4]
print(top(dizi))
