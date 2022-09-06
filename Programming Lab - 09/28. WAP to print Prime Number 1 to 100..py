print("Prime No 1 - 100 = ")
for i in range(1,101):
    count = 0
    
    for k in range(1,i+1):
        if i%k==0:
            count+=1
            
    if count==2:
        print(i,end=" ")
