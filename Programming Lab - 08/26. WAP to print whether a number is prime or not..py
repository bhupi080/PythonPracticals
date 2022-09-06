num = int(input("Enter any Number : "))
count = 0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if (count==2):
    print("Prime No ")
else:
    print("Not a Prime No ")
