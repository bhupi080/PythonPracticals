str = input("Enter any String : ")

l = str.split()
l1 = []
for i in range(0,len(l)):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])

output = " ".join(l1)
print(output)
