tup = ("KGF","Pushpa","Impossible")

# First Convert it into list
list1 = list(tup)

# Then Update
list1[2] = "1000Cr"

# Then again Convert back to Tuple
tup = tuple(list1)
print(tup)
print(type(tup))
