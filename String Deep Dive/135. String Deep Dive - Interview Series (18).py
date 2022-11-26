s = input("Enter any String : ")

v = ['a','e','i','o','u','A','E','I','O','U',]
d = {}

for ch in s:
    if ch in v:
        d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(f'{k} occurs {v} times')
