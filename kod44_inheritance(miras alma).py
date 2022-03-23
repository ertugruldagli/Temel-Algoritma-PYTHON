class kus():
    tur_Ad=""
    kus_ad=""

    def isimYaz(self):
        print("tür adı:",self.tur_Ad)
        print("kus adı:",self.kus_ad)

class yirtici(kus):
    print(kanat_uzunluğu="0")
    agirlik="0"

class kartal(yirtici):
    alt_tur=""

anadolu_kartali=kartal()

anadolu_kartali.tur_Ad="eagle"
anadolu_kartali.kus_ad="kara kartal"
anadolu_kartali.kanat_uzunluğu="1,5m"
anadolu_kartali.agirlik="6kg"
anadolu_kartali.alt_tur="güneydoğu"

anadolu_kartali.isimYaz()

