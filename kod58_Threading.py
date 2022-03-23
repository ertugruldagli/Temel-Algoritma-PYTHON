#Thread -  iş parçaçcığı
import threading

def d1():
    for i in range(10000):
        print("AAAAA", end=" ") # "end" komutu yan yana yazardırma işlemini gerçeklştirir.
def d2():
    for i in range(10000):
        print("BBBBB", end=" ")

t1= threading.Thread(target=d1)
t2= threading.Thread(target=d2)
t1.start()
t2.start()