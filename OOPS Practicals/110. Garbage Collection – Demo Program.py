import time

class Hang:
    def __init__(self):
        print("Object Initialization...")
    def __del__(self):
        print("Fulfilling Last Wish ")

ob=Hang()
ob=None
time.sleep(5)
print("End of application")
