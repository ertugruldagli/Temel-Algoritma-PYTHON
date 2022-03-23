import math

a=int(input("birinci kökü giriniz:"))
b=int(input("ikinci kökü giriniz:"))
c=int(input("Üçüncü kökü giriniz:"))

delta=b*b - (4*a*c)
print("delta sonucu:",delta)

if delta>0:
    kok1=(-(b)-math.sqrt(delta)) / 2*a
    kok2 = (-(b) + math.sqrt(delta)) / 2 * a
    print("Birinci kök",kok1)
    print("İkinci kök", kok2)
elif delta==0:
    kok=(-b)/(2*a)
    print("Cakışık kök var", kok)
else:
    print("kok yoktur")
