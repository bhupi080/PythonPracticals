


class Pushpa:
    a = 10
    def __init__(self):
        Pushpa.b = 20
    def m1(self):
        Pushpa.c = 30
    @classmethod
    def m2(cls):
        cls.d1 = 40
        Pushpa.d2 = 50
    @staticmethod
    def m3():
        Pushpa.e = 60

print(Pushpa.__dict__)
ob = Pushpa()
print(Pushpa.__dict__)
ob.m1()
print(Pushpa.__dict__)
Pushpa.m2()
print(Pushpa.__dict__)
Pushpa.m3()
print(Pushpa.__dict__)
Pushpa.f = 60
print(Pushpa.__dict__)





