string = input("Enter any Sentence : ")

lst = ['a','e','i','o','u']
mydict = {}

for char in string:
    if char in lst:
        c = string.count(char)
        mydict.update({char:c})
        
for keys,values in mydict.items():
    print(f"{keys} present in string {values} times ")
