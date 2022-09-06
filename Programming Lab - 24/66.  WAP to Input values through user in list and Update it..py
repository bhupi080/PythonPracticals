a = []
num = int(input("Enter Number of Values to be Entered : "))

# Input values in list (string)
for i in range(num):
    val = input(f"Enter the Value : at [{i}] ")
    a.append(val)

# Before Updating
print("You've Entered ")
print(a)

# Updating Operation
index = int(input("Enter the Index to Update Value : "))
if(index<num):
    updated_value = input("Enter the Updated Value : ")
    a[index] = updated_value
    print("After Updating")
    print(a)
else:
    print("Index Not found in List")
