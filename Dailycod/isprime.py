def isprime(n):
    if n < 0:
        return False
    a = []
    for i in range(1,n + 1 ):
        if n % i == 0:
            a.append(i)
    if a == [1,n]:
        return True
    else:
        return False      

print(isprime(10))