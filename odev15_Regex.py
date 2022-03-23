import re

s = "No. Wrong. Choice is an illusion, created between those with power," \
    " and those without. This is the nature of the universe. We struggle " \
    "against it, we fight to deny it, but it is of course pretense, it is a lie." \
    " Beneath our poised appearance, the truth is we are completely out of control. " \
    "Causality. There is no escape from it, we are forever slaves to it. Our only hope," \
    " our only peace is to understand it, to understand the 'why'. 'Why' is what separates " \
    "us from them, you from me. 'Why' is the only real social power, without it you are powerless." \
    " And this is how you come to me, without 'why', without power. Another link in the chain."
#1.SORU
a = re.findall("[ ]",s)
print(len(a))

#2.SORU
a = re.findall("[Why][why]",s)
print(len(a))

#3.SORU
a = re.findall("[.]",s)
print(len(a))

#4.SORU
a = re.search("Causality",s)
print(a)

#5.SORU
print(s.replace('Why','Causality').replace('Why','Causality'))

#6.SORU
a = re.split(" ",s)
print(a)

#7SORU
a = re.findall("i.", s)
print(a)

#8.SORU
a = re.findall("[aonudr]{3}",s)
print(a)

#9.SORU
a = re.findall(r'"(.*?)"', s)
print(a)

#10.SORU
a = re.findall("[,]",s)
print(len(a))

