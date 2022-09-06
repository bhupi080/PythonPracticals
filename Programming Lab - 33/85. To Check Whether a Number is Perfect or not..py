num = int(input("Enter any Number : "))
i=1
s=0
while(i<=num):
    s=s+i
    if s==num:
        print(num,"is Perfect Number")
        break
    i+=1
if i>num:
    print(num,"is not a Perfect Number")
