n = int(input("Enter Last No : "))

even_sum = 0
odd_sum = 0

print("\nEven Numbers = ",end = " ")
for i in range(1,n+1):
    if i % 2 == 0:
        print(i,end=" ")
        even_sum = even_sum + i
print("\nSum = ",even_sum)
        
print("\nOdd Numbers = ",end = " ")
for i in range(1,n+1):
    if i % 2 != 0:
        print(i,end=" ")
        odd_sum = odd_sum + i
print("\nSum = ",odd_sum)
