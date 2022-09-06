# Empty Dictionary
emp={}

num = int(input("Enter the keys to add : "))

# Input Keys,Values through keyboard
for i in range(num):
    line = input("Enter the key,value & Press Enter : ")
    eid,ename = line.split(",")
    emp.update({eid:ename})

print("You've Entered")
print(emp)

key = input("\nEnter the key you want to update : ")

# Checking if the key is present or not
if key in emp:
    value = input("Enter the value : ")
    emp[key] = value
    print("\nAfter Updating")
    print(emp)
else:
    print("Key not Found")
