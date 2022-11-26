s = input("Enter any String : ")
output = ""

for char in s:
    if char.isalpha():
        output+=char
        c = char
    else:
        d = int(char)
        newc = chr(ord(c)+d)
        output+=newc

print(output)
