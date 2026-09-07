def isarmstrong(x):
    res=0
    d=x
    if x<0:
        return False
    while x!=0:
        l=x%10
        x=x//10
        res=res+(l**3)
    if res==d:
        return True
    else:
        return False
print(isarmstrong(153))
        