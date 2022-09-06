n = int(input("Enter Number of lines "))

for row in range(n,0,-1):
    for spce in range(1,(n-row)+1):
        print(" ",end=" ")
    for star in range(1,(row*2-1)+1):
        print("*",end=" ")
    print()
