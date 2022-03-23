

dosya = open("asal.txt",mode="a",encoding='utf-8')

for sayi in range(2, 30):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                break
        else:
            dosya.write(str(sayi)+"\n")


dosya.close()

dosya = open("asal.txt",mode="r",encoding="utf-8")
print(dosya.read())
dosya.close()