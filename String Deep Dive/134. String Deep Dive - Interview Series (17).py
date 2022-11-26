s = input("Enter any String : ")

d = {}

for ch in s:
    d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(f'{k} occurs {v} times')
