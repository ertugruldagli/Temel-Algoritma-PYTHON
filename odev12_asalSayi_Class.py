class Asal:
       def asalmi(sayi):
              bolensayac = 0
              adet=0
              for i in range(2, s):

                     if s % i == 0:
                            bolensayac += 1

              if bolensayac >0:
                     return False
              else:
                     return True
       def oncekiasal(sayi):
              adet = 0
              bolensayac = 0
              for i in range(2,s):

                     if s % i == 0:
                            bolensayac += 1
              if bolensayac >0:
                     return False
              else:
                     return True

a = Asal()
s=int(input("sayi giriniz:"))
print(a.asalmi())
print(a.oncekiasal())



