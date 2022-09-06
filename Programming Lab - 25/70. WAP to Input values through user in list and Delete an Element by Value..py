a = []
num = int(input("Enter Number of Values to be Entered : "))

# Input values in list (int)
for i in range(num):
    val = int(input(f"Enter the Value : at [{i}] "))
    a.append(val)

# Before Deletion 
print("You've Entered ")
print(a)

# Deletion Operation by value
value = int(input("Enter the Value to Delete : "))

if value in a:
    a.remove(value)
    print("After Deleting Value")
    print(a)
else:
    print("Value not Found")
