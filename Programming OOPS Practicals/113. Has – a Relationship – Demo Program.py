



class Engine:
    oil="Full"
    def __init__(self):
        self.signal="Go"
    def start(self):
        print('Engine Starts ')

class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('Car using Engine Class ')
        print(self.engine.oil)
        self.engine.start()
        print(self.engine.signal)

c=Car()
c.m2()

