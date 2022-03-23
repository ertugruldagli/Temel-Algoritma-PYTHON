#ilk 10 asalı txt dosyaya yazdıralım

def asalMi(sayi):
    bs = 0
    for i in range(2, sayi):
        if (sayi % i == 0):
            bs += 1
    if bs == 0:
        return True
    else:
        return False

dosya = open("asal.txt",mode="w",encoding="utf-8")
sayac = 0
sayi = 1
while True:
    sayi += 1
    if(asalMi(sayi)):
        dosya.write(str(sayi)+"\n")
        sayac+=1
        if(sayac==100):
            break


dosya.close()