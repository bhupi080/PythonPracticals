a = []
num = int(input("Enter Number of Values to be Entered : "))

# Input values in list (string)
for i in range(num):
    val = input(f"Enter the Value : at [{i}] ")
    a.append(val)

# Before Inserting
print("You've Entered ")
print(a)

# Inserting Operation
index = int(input("Enter the Index to Insert: "))
if(index<num):
    value = input("Enter the Value : ")
    a.insert(index,value)
    print("After Inserting")
    print(a)
else:
    print("Index Not found in List")
