num1 = int(input("Enter 1st No : "))
num2 = int(input("Enter 2nd No : "))

s = lambda a,b : a if a>b else b
print("Bigger is : ",s(num1,num2))
