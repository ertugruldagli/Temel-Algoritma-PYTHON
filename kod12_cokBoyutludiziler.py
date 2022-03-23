#çok boyutlu diziler

m = [[1,3,4], #yatay da yazılabilir
     [2,0,1], #anlaşılması için matris formuna döndürdüm
     [0,1,2]]

print(m)
#print(m[1][3]) #taşma hatası
print(m[1][2])

#print(m[1]) #pythonda satır satır da yazılır

for i in range(3):
    print(m[i])
