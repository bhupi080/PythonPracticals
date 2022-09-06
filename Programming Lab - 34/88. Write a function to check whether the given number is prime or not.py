num = int(input("Enter any Number : "))

def cprime(a):
    count = 0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if (count==2):
        return "Prime No "
    else:
        return "Not a Prime No "

print(cprime(num))
