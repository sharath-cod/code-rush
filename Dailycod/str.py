for i in range (5):
    for j in range(5):
        print(" *", end=" ")
    print()


for i in range(6):
    for j in range (i):
        print(" *", end=" ")
    print()



for i in range (5, 0, -1):
    for j in range (i):
        print(" *", end =" ")
    print()

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)


for i in range (5):
    for j in range(5):
        print(i+1, end=" ")
    print()


for i in range(6):
    for j in range (i):
        print(j+1, end=" ")
    print()



for i in range (5, 0, -1):
    for j in range (i):
        print(j+1, end =" ")
    print()

n=5
for i in range(1,n+1):
    print(" "*(n-i)+f"{i} "*i)

n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)


n=5
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

n=5
for i in range(1,n+1):
    for j in range(i):
        if((i+j)%2==0):
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

n=5
for i in range (5):
    for j in range(i):
        print(j+1, end=" ")
    print()
    for j in range(i):
        print(" "*(n-i)+f"{i} "*i)
    print()
      
n=5
for i in range(n):
    for j in range(i):
        print(j+1, end=" ")
    for j in range (2*(n-i)):
        print(" ", end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()


n=6
c=1
for i in range(n):
    for j in range(i):

        print(c, end=" ")
        c+=1
    print()

n=5
for i in range(n):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()

n=5
for i in range(0,n):
    for j in range(i):
        print(chr(65+i)+" ", end=" ")
    print()

    n=5
for i in range(2*n-1):
    if(i<n):
         for j in range(i+1 ):
             print("*",end=" ")
    else:
        for j in range(2*n-i-1):
                print("*",end=" ")
    print()


n=4
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j, end="")
    s=2*(n-i)
    print(" "*s,end="")
    for j in range (i,0,-1):
        print(j,end="")
    print()


    n = 5
for i in range(1,n+1):
    # Left stars
    for j in range(i):
        print("*", end="")
    
    # Spaces in the middle
    spaces = 2*(n-i)
    print(" " * spaces, end="")
    
    # Right stars
    for j in range(i):
        print("*", end="")
    