string = input("Enter Any String : ")
dic = {}
for char in string:
    c = string.count(char)
    dic.update({char:c})

for keys,values in dic.items():
    print(f"{keys} present in string {values} times ")
