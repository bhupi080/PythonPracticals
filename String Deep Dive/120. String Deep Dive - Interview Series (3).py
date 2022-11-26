str = input("Enter any String : ")

lst = str.split()
lst1 = []

for word in lst:
    lst1.append(word[::-1])

output=" ".join(lst1)
print(output)
