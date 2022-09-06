num = int(input("Enter Last Number : "))

s = 0

for i in range(1,num+1):
    count = 0
    
    for k in range(1,i+1):
        if i%k==0:
            count+=1
            
    if count==2:
        print(i,end=" ")
        s+=i

print("\nSum = ",s)
