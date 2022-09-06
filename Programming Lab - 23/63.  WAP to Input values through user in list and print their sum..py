a = []
sum = 0
num = int(input("Enter Number of Values to be Entered : "))

for i in range(num):
    val = int(input("Enter the Value : "))
    a.append(val)
    sum = sum + a[i]

print(a)
print("Sum = ",sum)
    
