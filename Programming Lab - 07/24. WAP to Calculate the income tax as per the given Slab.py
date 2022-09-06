income = int(input("Enter your Annual Income : "))
tax = 0

if(income<=250000):
    tax = 0
elif(income<=500000):
    tax = (income - 250000)*5/100
elif(income<=1000000):
    tax = 250000*5/100
    tax = tax + (income - 500000)*20/100
elif(income>1000000):
    tax = 250000*5/100
    tax = tax + 500000*20/100
    tax = tax + (income - 1000000)*30/100

cess = tax*1/100

print("\n Tax          = ",tax)
print("\n Cess @1%     = ",cess)
print("\n Total Payble = ",tax + cess)
