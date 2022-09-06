a = []
num = int(input("Enter Number of Values to be Entered : "))

# Input values in list (string)
for i in range(num):
    val = input(f"Enter the Value : at [{i}] ")
    a.append(val)

# Before Deletion 
print("You've Entered ")
print(a)

# Deletion Operation by index
index = int(input("Enter the Index to Delete : "))

if(index<num):
    del a[index]
    print("After Deleting")
    print(a)
else:
    print("Index not Found")
