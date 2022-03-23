s = input("iki basamaklı bir sayi giriniz: ")

d_birler = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 0: "" }
d_onlar = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC", 0: ""}

onlar = int(s[0])
birler = int(s[1])


print(d_onlar[onlar],d_birler[birler])






