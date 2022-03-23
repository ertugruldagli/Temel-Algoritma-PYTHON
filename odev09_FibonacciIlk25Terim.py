
dizi = []
a = 1
b = 1
c = 1
dizi.append(a)
dizi.append(b)
while len(dizi)<=24:
    c = a+b
    a = b
    b = c

    dizi.append(b)

print(dizi)