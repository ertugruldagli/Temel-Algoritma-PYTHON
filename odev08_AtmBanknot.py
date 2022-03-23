while True:
    s=int(input("miktar giriniz:"))
    b=[200,100,50,20,10]

    if s%10==0:
        for i in range (len(b)):
            if s>=b[i]:
                adet=s//b[i]
                s=s%b[i]
                print(f"{adet} adet {b[i]}")
        break
    else:
     print("10'un katını giriniz!!")