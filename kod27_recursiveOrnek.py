dizi=[0,1,4,2,5]
def dizitop(dizi):
    if len(dizi)==1:
        return dizi[0]
    else:
        return dizi[0]+dizitop(dizi[1:])

print(dizitop(dizi))

