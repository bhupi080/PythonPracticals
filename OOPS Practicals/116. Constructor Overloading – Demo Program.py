class Parent:
    def __init__(self):
        print("Parent Class Constructor")

class Child(Parent):
    def __init__(self):
        print("Child class Constructor")

obj = Child()
