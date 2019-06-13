def f(x:"kg") -> "int type":
    return x**2

print(f(4))
print(f.__annotations__)

def f2(x):
    pass
print(f2(12))

class animal:
    def say(self):
        print("animal say")

class dog:
    def __init__(self):
        self.a : animal = animal()
        self.b = 6
    def showdict(self):
        print(self.__dict__.values())
    def sets(self, key, value):
        object.__setattr__(self,key,value)


d1 = dog()
d1.a.say()
print(type(d1.a))

print("-----------------")
d1.showdict()
d1.sets("age",12)
d1.showdict()

print(False and 1)

