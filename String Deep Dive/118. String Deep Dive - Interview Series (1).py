

str = input("Enter any String : ")
new = ""

for i in range(0,len(str)):
    if str[i].islower():
        new = new + str[i].upper()
    elif str[i].isupper():
        new = new + str[i].lower()
    else:
        new = new + str[i]

print("After Swapcase = ",new)







