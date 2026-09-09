def divisors(n):
    if n < 0:
        return 0
    a = []
    for i in range(1,n + 1 ):
        if n % i == 0:
            a.append(i)
    return a
print(divisors(100))