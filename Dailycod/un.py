
n = 5
for i in range(2*n):
    if(i<n):
        for j in range(i):
            print("*", end="")
    
    # Spaces in the middle
        spaces = 2*(n-i)
        print(" " * spaces, end="")
    
        # Right stars
        for j in range(i):
            print("*", end="")
        print()
    else:
    # Left stars
        for j in range(n,0,-1):
            print("*", end="")
    
    # Spaces in the middle
        spaces = 2*n-i
        print(" " * spaces, end="")
    
    # Right stars
        for j in range(i):
            print("*", end="")
        print()