a=int(input("birinci sayi giriniz:"))
b=int(input("ikinci sayi giriniz:"))
c=int(input("Üçüncü sayi giriniz:"))

if a>b and a>c:
    print("en büyük sayi", a)
elif b>a and b>c:
    print("en büyük sayi",b)
else:
    print("en büyük sayi",c)