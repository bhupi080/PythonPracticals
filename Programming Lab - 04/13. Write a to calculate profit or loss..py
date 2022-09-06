cost = int(input("Enter Cost Price : "))
sell = int(input("Enter Selling Price : "))

if sell > cost: 
  print("Profit") 
elif cost > sell: 
  print("Loss")
else:
    print("No Profit No Loss")
