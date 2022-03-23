ikikat= lambda x:x*2
print(ikikat(5))

liste=[1,4,7,6,9,2,5,8,3,0]

ylist= list(filter(lambda x:x%2==1,liste))
print(ylist)

ylist2=list(map(lambda x:x*3,liste))
print(ylist2)