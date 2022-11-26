
class Pushpa:
    a = 10
    def __init__(self):
        Pushpa.b = 20
        del Pushpa.a
    def m1(self):
        Pushpa.c = 30
        del Pushpa.b

    @classmethod
    def m2(cls):
        cls.d = 40
        del Pushpa.c

    @staticmethod
    def m3():
        Pushpa.e = 50
        del Pushpa.d

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
del Pushpa.e
print(Pushpa.__dict__)
