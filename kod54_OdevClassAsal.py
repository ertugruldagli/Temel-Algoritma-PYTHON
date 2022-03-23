class Asal:
    def asalMi(self,sayi):
        bs = 0
        for i in range(2,sayi):
            if(sayi%i==0):
                bs+=1
        if bs==0:
            return True
        else:
            return False

    def oncekiAsal(self,sayi):
        oasal = 0
        while True:
            sayi-=1
            if self.asalMi(sayi):
              oasal=sayi
              break
        return oasal

    def sonrakiAsal(self,sayi):
        sasal=0
        while True:
            sayi+=1
            if self.asalMi(sayi):
              sasal=sayi
              break
        return sasal

a = Asal()
sayi = int(input("Bir sayı giriniz:"))
print(a.asalMi(sayi))
print(a.oncekiAsal(sayi))
print(a.sonrakiAsal(sayi))
