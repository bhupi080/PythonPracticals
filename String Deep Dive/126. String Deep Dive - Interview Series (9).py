
str = input("Enter any String : ")

i=0
print("Even index = ",end=" ")
while i<len(str):
    print(str[i],end=" ")
    i+=2

i=1
print("\nOdd index = ",end=" ")
while i<len(str):
    print(str[i],end=" ")
    i+=2
