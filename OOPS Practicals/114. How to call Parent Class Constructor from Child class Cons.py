class Parent:
    def __init__(self):
        print("Parent Class Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class Constructor")

obj = Child()
