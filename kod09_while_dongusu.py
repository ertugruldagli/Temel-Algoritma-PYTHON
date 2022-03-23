#i=0
#while i<10:
   # i+=1

bas=int(input("bas sayıyı giriniz:"))
bitis=int(input("bitis sayıyı giriniz:"))

tektoplam=cifttoplam=0
teksayac=ciftsayac=0

while bas<bitis:
    if bas%2==0:
        cifttoplam+=bas
        ciftsayac+=1
    else:
        tektoplam+=bas
        teksayac+=1
    bas+=1
ciftort = cifttoplam / ciftsayac
tekort = tektoplam / teksayac

print("Çift toplam =",cifttoplam)
print("Çift adet =",ciftsayac)
print("Çift ortalama =",ciftort)

print("Tek toplam =",tektoplam)
print("Tek adet =",teksayac)
print("Tek ortalama =",tekort)