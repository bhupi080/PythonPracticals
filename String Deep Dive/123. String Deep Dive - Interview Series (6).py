str = input("Enter any String : ")
output = 0

for i in range(0,len(str)):
    if str[i].isdigit():
        output += int(str[i])

print("Sum = ",output)
