even = []
odd = []

num = int(input("Enter Last Number : "))

print("Even Number ",end=" ")
for i in range(1,num+1):
    if i%2==0:
        even.append(i)
print(even)

print("Odd Number ",end=" ")
for i in range(1,num+1):
    if i%2!=0:
        odd.append(i)
print(odd)
