def fil(x):
    if x%5==0:
        return True
 
a = [2, 5, 7, 8, 10, 13, 16]
 
result = filter(fil, a)

print('Original List :', a)
print('Filtered List :', list(result))
