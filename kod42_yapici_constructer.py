class cokgen:
    def __init__(self,yukseklik,genislik):
        self.yukseklik=yukseklik #initialize başlangıç değeri
        self.genislik=genislik

    def alan(self):
        return self.genislik*self.yukseklik
nesne=cokgen(15,25)#constructer method burada çalışır.
print(nesne.alan())