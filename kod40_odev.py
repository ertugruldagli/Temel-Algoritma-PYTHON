#0-10 arasında 100 adet rastgele sayıdan oluşan
# bir dizi üretip return eden
import random as r

def uret():
    dizi = []
    # dizi = [random.randint(0,10) for i in range(100)]
    for i in range(100):
        dizi.append(r.randint(0,10))
    return dizi

print(uret())