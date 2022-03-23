d=open("deneme.txt",mode='w',encoding='utf-8')
#w=write
#r=read
#a=apped
for i in range(50):
    d.write(str(i)+".satir\n")

d.close()

d=open("deneme.txt",mode='r',encoding='utf-8')
print(d.read())
d.close()