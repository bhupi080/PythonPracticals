num = int(input("Enter Any Number : "))
temp = num
count=0 

# calculating Number of Digits
while(num>0):
    r = num%10
    count+=1
    num = num//10
print("Digits :",count)

# Calculating Power
num = temp
while(num>0):
    r = num%10
    print(r,"=",r**count)
    num = num//10
