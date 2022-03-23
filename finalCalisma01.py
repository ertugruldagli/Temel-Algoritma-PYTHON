x=12 #global
def fonksiyon():
    x=15 #local
    print("local olan:",x)
fonksiyon()
print("global olan:",x)

sayi=3
def fonk():
    global sayi
    sayi=sayi*10
    print("carpim:",sayi)
fonk()