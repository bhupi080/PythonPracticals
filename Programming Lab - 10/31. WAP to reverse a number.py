num = int(input("Enter Last Number : "))

sumr=0

while(num>0):
    r = num%10
    sumr = sumr*10+r
    num = num//10

print("Reverse : ",sumr)
