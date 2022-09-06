for row in range(1,5):
    for spce in range(1,(5-row)+1):
        print(" ",end=" ")
    for star in range(1,(row*2-1)+1):
        print("*",end=" ")
    print()

for row in range(5,0,-1):
    for spce in range(1,(5-row)+1):
        print(" ",end=" ")
    for star in range(1,(row*2-1)+1):
        print("*",end=" ")
    print()
