str = input("Enter any String : ")

alpha = []
digit = []

for char in str:
    if char.isalpha():
        alpha.append(char)
    else:
        digit.append(char)

output = "".join(sorted(alpha)+sorted(digit))
print(output)
