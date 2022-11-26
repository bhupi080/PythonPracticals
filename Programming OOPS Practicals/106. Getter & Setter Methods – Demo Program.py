


class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setGf(self,gf):
        self.gf=gf

    def getGf(self):
        return self.gf

n=int(input('Enter number of Entries:'))

for i in range(n):
    s=Student()
    name=input('Enter Name:')
    s.setName(name)
    gf=input('Enter GF:')
    s.setGf(gf)
    print('Hi',s.getName())
    print('Your GirlFriend Name:',s.getGf())
    print()












