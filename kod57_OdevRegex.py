s = "No. Wrong. Choice is an illusion, created between those with power," \
    " and those without. This is the nature of the universe. " \
    "We struggle against it, we fight to deny it, but it is of course pretense, " \
    "it is a lie. Beneath our poised appearance, the truth is we are completely" \
    " out of control. Causality. There is no escape from it, we are forever " \
    "slaves to it. Our only hope, our only peace is to understand it, " \
    "to understand the 'why'. 'Why' is what separates us from them, you from me." \
    " 'Why' is the only real social power, without it you are powerless." \
    " And this is how you come to me, without 'why', " \
    "without power. Another link in the chain."

import re

#1. Kaç adet boşluk vardır? Regex ifesedesini yazınız?
a = re.findall("[\s]",s)
print("1.",len(a))
#2. why/Why sözcüklerinin adetini bulan regex ifadesini yazınız?
a = re.findall("[Wwhy]{3}",s)
print("2.",len(a))
#3. Nokta sayısını bulan regex ifadesini yazınız?
a = re.findall("[\.]",s)
print("3.",len(a))
#4. Causality kelimesinin konumunu bulunuz? (re.search())
a = re.search("Causality",s)
print("4.",a)
#5. Tüm why/Why kelimelerinin yerine causality yazdınırız? (replace-> re.sub())
a = re.sub("[Wwhy]{3}","causality",s)
print("5.",a)
#6. Tüm sözcükleri boşluktan parçalıyınız? (split)
a = re.split("[\s]",s)
print("6.",a)
#7. a = re.findall("i.",s)  -> a dizisinde neler listelenir?
a = re.findall("i.",s)
print("7.",a)
#8. a = re.findall("[aonudr]{3}",s) -> a dizisinde neler listelenir?
a = re.findall("[aonudr]{3}",s)
print("8.",a)
#9. a = re.findall(r'"(.*?)"', s) -> a dizisinde neler listelenir?
a = re.findall("(.*?)", s)
print("9.",a)
#10. Virgül sayısını bulan regex ifadesini yazınız?
a = re.findall("[\,]",s)
print("10.",len(a))