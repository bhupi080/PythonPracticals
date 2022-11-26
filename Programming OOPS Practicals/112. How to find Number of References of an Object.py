
import sys
class Pushpa:
    pass

t1 = Pushpa()
t2 = t1
t3 = t2
t4 = t3

print(sys.getrefcount(t1))
