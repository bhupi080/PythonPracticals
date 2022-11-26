
s = input("Enter any String : ")
prev = s[0]
output = ""
c=1
i=1

while i<len(s):
    if s[i]==prev:
        c+=1
    else:
        output += str(c)+prev
        prev = s[i]
        c=1
    if i == len(s)-1:
        output += str(c) + prev
    i+=1

print(output)
