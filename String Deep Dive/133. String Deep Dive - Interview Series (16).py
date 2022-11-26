s = input("Enter any String : ")
output = ""

for ch in s:
    if ch not in output:
        output+=ch

print(output)
