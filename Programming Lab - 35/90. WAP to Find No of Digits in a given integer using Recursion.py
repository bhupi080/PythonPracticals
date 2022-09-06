count=0
def count_digit(num):
    global count
    if (num != 0):
        count +=1
        count_digit(num // 10)
    return count

n=int(input("Enter a number : "))
print("The number of digits is :",count_digit(n))
