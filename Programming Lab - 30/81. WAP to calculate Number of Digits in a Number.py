num = int(input("Enter Any Number : "))

count=0 

while(num>0):
    r = num%10
    count+=1
    num = num//10

print("Digits : ",count)
