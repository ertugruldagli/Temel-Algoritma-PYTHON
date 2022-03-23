from tkinter import*
def yaz(x):
    s=len(giris.get())
    giris.insert(s, str(x))

hesap=5
sayi=0

def islemler(x):
    global hesap
    hesap=x
    global sayi
    sayi=float(giris.get())
    print(hesap)
    print(sayi)
    giris.delete(0,'end')

sayi2=0
def hesapla():
    global sayi2
    sayi2=float(giris.get())
    print(sayi2)
    global hesap
    soncu=0
    if(hesap==0):
        sonuc=sayi+sayi2
    elif(hesap==1):
        sonuc=sayi-sayi2
    elif (hesap == 2):
        sonuc = sayi*sayi2
    elif (hesap == 3):
        sonuc = sayi/sayi2
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))

pencere = Tk()
pencere.geometry("250x350")
giris = Entry(fg ="BROWN",font="Verdana 12",width=20,justify=RIGHT)
giris.place(x=20,y=20)

b = []
for i in range(1,10):
    b.append(Button(text=str(i),fg ="BLUE",font="Verdana 12",command=lambda x=i:yaz(x)))
sayac=0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1
islem = []
for i in range(0,4):
    islem.append(Button(fg ="orange",font="Verdana 12",width=2,command=lambda x=i:islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0,4):
    islem[i].place(x=170,y=50+50*i)

sb = Button(text="0",font="Verdana 12",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)
nb = Button(text=".",font="Verdana 12",width=2,command=lambda x=".":yaz(x))
nb.place(x=70,y=200)
eb = Button(text="=",fg ="RED",font="Verdana 12",command=hesapla)
eb.place(x=120,y=200)

pencere.mainloop()