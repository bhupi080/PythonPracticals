num = int(input("Enter Any Number : "))
temp = num
count=0 

# calculating Number of Digits
while(num>0):
    r = num%10
    count+=1
    num = num//10

sum = 0
# Calculating Power
num = temp
while(num>0):
    r = num%10
    sum = sum + r**count
    num = num//10

if(temp==sum):
    print("Amstrong Number")
else:
    print("Not an Amstrong Number")
