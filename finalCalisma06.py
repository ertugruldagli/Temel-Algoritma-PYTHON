import math


class Geometri:
    yukseklik = 10
    genislik = 10
    yaricap = 5
    alan = 5  # global
    cevre = 0

    def kareAlan(self, yukseklik, genislik):
        global alan
        alan = yukseklik * genislik  # local
        return alan

    def daireCevre(self):
        return 2 * math.pi * self.yaricap

    def daireAlan(self, yaricap):
        return math.pi * yaricap ** 2


g = Geometri()
print(g.kareAlan(25, 15))
print(g.daireCevre())
print(g.daireAlan(6))