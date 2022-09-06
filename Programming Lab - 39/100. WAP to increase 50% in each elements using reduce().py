from functools import reduce

def sum(a):
    return a

scores = [10, 20, 30, 40, 50]

total = reduce(sum, scores)
print(total)
