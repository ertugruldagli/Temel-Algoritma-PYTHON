print(chr(65))
print(ord('A'))

print(chr(97))
print(ord('h'))

import random
s=""

for i in range(5):
    s+= chr(random.randint(65,90))

print(s)