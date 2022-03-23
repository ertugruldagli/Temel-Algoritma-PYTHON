vize=int(input("Vize notunu giriniz:"))
final=int(input("Final notunu giriniz:"))

puan = (vize*0.4)+(final*0.6)
print(puan)

if puan>=90 and puan<=100:
    print("AA")
elif puan>=85 and puan<=89:
    print("BA")
elif puan >= 75 and puan <= 84:
    print("BB")
elif puan>=70 and puan<=74:
    print("CB")
elif puan>=60 and puan<=69:
    print("CC")
elif puan>=55 and puan<=59:
    print("DC")
    print("Şartlı geçti.")
elif puan>=50 and puan<=54:
    print("DD")
    print("kaldı.")
elif puan>=40 and puan<=49:
    print("FD")
    print("kaldı.")
elif puan>=0 and puan<=39:
    print("FF")
    print("kaldı.")
else:
    print("F")
    print("kaldı.")

