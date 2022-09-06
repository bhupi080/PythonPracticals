# Empty Dictionary
emp={}

num = int(input("Enter the keys to add : "))

# Input Keys,Values through keyboard
for i in range(num):
    line = input("Enter the key,value & Press Enter : ")
    eid,ename = line.split(",")
    ename = int(ename)
    emp.update({eid:ename})

print("You've Entered")
print(emp)

# Sum of Values
print(sum(emp.values()))


