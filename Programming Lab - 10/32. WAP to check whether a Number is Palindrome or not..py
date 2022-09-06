num = int(input("Enter any Number : "))

sumr=0
temp = num
while(num>0):
    r = num%10
    sumr = sumr*10+r
    num = num//10

if (temp == sumr):
    print("Pallindrome")
else:
    print("Not a Pallindrome")
