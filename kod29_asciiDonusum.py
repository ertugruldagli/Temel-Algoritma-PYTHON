#kullanıcıdan büyük harf ingiliz alfabesi ile
#ismini alıp
#ismindeki harflerin sayısal karşığını fonksiyon ile bulalım

s=input("isminizi giriniz:")
def asciiDonusum(s):
    for i in s:
     print(ord(i))
asciiDonusum(s)

