



class Pushpa:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
    def m1(self):
        del self.d

ob = Pushpa()
print(ob.__dict__)
ob.m1()
print(ob.__dict__)
del ob.c
print(ob.__dict__)






