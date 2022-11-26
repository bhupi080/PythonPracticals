



class Pushpa:
    a = 10
    def __init__(self):
        print(self.a)
        print(Pushpa.a)
    def m1(self):
        print(self.a)
        print(Pushpa.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Pushpa.a)
    @staticmethod
    def m3():
        print(Pushpa.a)

ob = Pushpa()
print(Pushpa.a)
print(ob.a)
ob.m1()
ob.m2()
ob.m3()









