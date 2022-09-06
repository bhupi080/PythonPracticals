num = int(input("Enter Any Number : "))

# variable to store Sum
s=0 

while(num>0):
    r = num%10
    if r%2!=0:
        s = s+r
    num = num//10

print("Sum (Odd Digit): ",s)


