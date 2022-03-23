class urun:

    def __init__(self):
        self.__fiyat=1000 #fiyat değişkeni __ ile kapsülleme

    def fiyatYaz(self):
        print("ürün fiyatı:", self.__fiyat)

    def setFiyat(self,fiyat):
        self.__fiyat=fiyat



u=urun()
u.fiyatYaz()

u.__fiyat=900
u.fiyatYaz()

u.setFiyat(50)
u.fiyatYaz()

