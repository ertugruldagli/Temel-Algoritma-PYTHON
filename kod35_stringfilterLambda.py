s = "melisa"

cift = list(filter(lambda x:ord(x)%2==0,s))
print(cift)

tek = list(filter(lambda x:ord(x)%2==1,s))
print(tek)