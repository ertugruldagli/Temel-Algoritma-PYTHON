def fak(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fak(n-1)
print(fak(5))