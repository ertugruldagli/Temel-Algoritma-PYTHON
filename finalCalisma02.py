class ogrenci:
    ad="ertu"
    soyad="dgl"
    vize=57
    final=100

    def isim(self):
        print(self.ad)
        print(self.soyad)


    def ort(self):
        return (self.vize*0.4) + (self.final*0.6)

o=ogrenci()
o.isim()
#o.isim("murteza")
print(o.ort())