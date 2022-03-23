ad="ali"
soyad="öz"

class ogrenci:
   # global ad, soyad global değişken kullanılacaksa buraya yazılır.
    ad= "ertu" #local
    soyad="can"
    #v=50
    #f=70

    def yazdir(self):
        print(self.ad)
        print(self.soyad)
       # print(ad,soyad)

    def ortalama(self,v,f):
        #return self.v*0,4+self.f*0,6 #localdaki v ve f değişkenleri için
        return v*0.4+f*0.6

nesne = ogrenci()

print(nesne.ad)

nesne.ad="yasin"
print(nesne.ad)

nesne.yazdir()

print(nesne.ortalama(55,60))