# kullanıcıdan 0 ve 100 arasında sayı girmeyi zorlayuınız. Vize final örneği

v= int(input("vize notunu giriniz:"))

while True:

    if v>=0 and v<=100:
        break
    else:
        print("aralıkta sayı giriniz:")
        v = int(input("vize notunu giriniz:"))


f= int(input("final notunu giriniz"))

while True:

    if f>=0 and f<=100:
        break
    else:
        print("aralıkta sayı giriniz")
        f = int(input("final notunu giriniz"))


o=(v*0.4)+(f*0.6)
print("Ortalaması", o)
