str = input("Enter any String : ")
output = ""

i = len(str)-1
while(i>=0):
    output+=str[i]
    i-=1
print(output)
