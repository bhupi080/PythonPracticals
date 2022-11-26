# string followed by digits
str = input("Enter any String : ")

output = ""
for char in str:
    if char.isalpha():
        c = char
    else:
        d = int(char)
        output+=c*d

print("".join(sorted(output)))
