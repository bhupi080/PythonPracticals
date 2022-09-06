a = []
num = int(input("Enter Number of Values to be Entered : "))

# Input values in list (int)
for i in range(num):
    val = int(input(f"Enter the Value : at [{i}] "))
    a.append(val)

print("You've Entered ")
print(a)

# Search Operation
search = int(input("Enter the Value to Search : "))

flag = 0
# Searching the value
for i in range(num):
    if(a[i]==search):
        flag = 1
        break

if flag==1:
    print("Value Found at Index = ",i)
else:
    print("Value Not Found")
