s = " Eğer, bütün etrafındakiler panik içine düştüğü ve bunun sebebini senden bildikleri zaman sen başını dik tutabilir ve sağduyunu kaybetmezsen; Eğer sana kimse güvenmezken sen kendine güvenir ve onların güvenmemesini de haklı görebilirsen; Eğer beklemesini bilir ve beklemekten de yorulmazsan veya hakkında yalan söylenir de sen yalanla iş görmezsen, ya da senden nefret edilir de kendini nefrete kaptırmazsan, bütün bunlarla beraber ne çok iyi ne de çok akıllı görünmezsen; Eğer hayal edebilir de hayallerine esir olmazsan, Eğer düşünebilip de düşüncelerini amaç edinebilirsen, Eğer zafer ve yenilgi ile karşılaşır ve bu iki hokkabaza aynı şekilde davranabilirsen; Eğer ağzından çıkan bir gerçeğin bazı alçaklar tarafından ahmaklara tuzak kurmak için eğilip bükülmesine katlanabilirsen, ya da ömrünü verdiğin şeylerin bir gün başına yıkıldığını görür ve eğilip yıpranmış aletlerle onları yeniden yapabilirsen; Eğer bütün kazancını bir yığın yapabilir ve yazı-tura oyununda hepsini tehlikeye atabilirsen; ve kaybedip yeniden başlayabilir ve kaybın hakkında bir kerecik olsun bir şey söylemezsen; Eğer kalp, sinir ve kasların eskidikten çok sonra bile işine yaramaya zorlayabilirsen ve kendinde 'dayan' diyen bir iradeden başka bir güç kalmadığı zaman dayanabilirsen; Eğer kalabalıklarda konuşup onurunu koruyabilirsen, ya da krallarla gezip karakterini kaybetmezsen; Eğer ne düşmanların ne de sevgili dostların seni incitmezse; Eğer aşırıya kaçmadan tüm insanları sevebilirsen; Eğer bir daha dönmeyecek olan dakikayı, altmış saniyede koşarak doldurabilirsen; Yeryüzü ve üstündekiler senindir Ve dahası sen bir İNSAN olursun oğlum..."

import re

a= re.findall("[Eğer]{4}",s)
print("1.",len(a))

a = re.findall("[.,;]",s)
print("2.",len(a))

a=re.sub("Eğer","if",s)
#print("3.",a)

a=re.split("[\;]",s)
#print("4.",a)

a = re.findall("[çğıüöş]",s)
print("5.",len(a))

a = re.findall("[\s]",s)
print("6.",len(a))

a = re.findall("[A-Z]",s)
print("7.",len(a))

a = re.findall("[\s]",s)
print("8.",len(a)+1)

a = re.findall("[A-Z|a-z]",s)
m= re.findall("[a,e,ı,i,o,ö,u,ü|A,E,I,I,O,O,U,U]",s)
print("9.",len(a)-len(m))

a= re.findall("[i,ö,ç,ü,ş,ğ]{2}",s)
m= re.findall(".i|i.|ü.|.ü|.ğ|ğ.|ş.|.ş|ö.|.ö|ç.|.ç",s)
print("10.",len(m))
print("10.",len(a))






