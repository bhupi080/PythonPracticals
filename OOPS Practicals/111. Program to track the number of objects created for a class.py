class Pushpa:
    count=0
    def __init__(self):
        Pushpa.count =Pushpa.count+1
    @classmethod
    def noOfObjects(cls):
        print('The number of objects created',cls.count)

t1=Pushpa()
t2=Pushpa()
Pushpa.noOfObjects()
t3=Pushpa()
t4=Pushpa()
t5=Pushpa()
Pushpa.noOfObjects()
