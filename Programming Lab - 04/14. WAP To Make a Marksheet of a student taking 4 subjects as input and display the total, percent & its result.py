s1 = int(input("Enter your marks in Maths : "))
s2 = int(input("Enter your marks in Science : "))
s3 = int(input("Enter your marks in Eng : "))
s4 = int(input("Enter your marks in Hindi : "))
s5 = int(input("Enter your marks in Maths: "))

total = s1+s2+s3+s4+s5

per = (total/500)*100
print("\nTotal Marks = ",total)
print("Percent = {:.2f}".format(per))

if per>=33:
    print("Result = Pass")
else:
    print("Result = Fail")
    
