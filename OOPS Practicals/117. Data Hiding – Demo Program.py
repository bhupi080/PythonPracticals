class Account:
    def __init__(self,initial_balance):
        self.__balance = initial_balance
    def getBalance(self):
        return self.__balance

a = Account(10000)
print(a.getBalance())
