num = int(input("Enter Any Number : "))

count=0 

while(num>0):
    r = num%10
    print("Cube of",r,"=",r**3)
    num = num//10
