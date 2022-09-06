f1 = 0
f2 = 1

i=1
while(i<=10):
    print(f1,end=" ")
    fn = f1 + f2
    f1 = f2
    f2 = fn
    i+=1
