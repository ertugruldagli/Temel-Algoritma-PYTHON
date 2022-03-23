#kendisine gönderilen string içindeki
#karakterleri tek- çift ayıran fonksiyon

def ayirma(s):
    tek=[]
    cift=[]
    for i in range(len(s)):
        if ord(s[i]) % 2 == 0:
            cift.append(ord(s[i]))
            cift.append(s[i])
        else:
            tek.append(ord(s[i]))
            tek.append(s[i])
    print(cift)
    print(tek)


s = input("Bir string giriniz:")
ayirma(s)
