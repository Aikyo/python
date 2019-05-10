

print(hash("string"))
print(hash("string"))
print(hash(2))

class student:
    #hello
    age = 13
    _weight = 13
    hobits = []   #类变量
    def __init__(self,name):
        global  age
        self.name = name   #对象变量
    def show(self,greeding):
        print(greeding)


"""
#对象b试图修改一个mutable的变量，则python找到类Man的__dict__中的变量lis，
#由于lis是可以修改的，因此直接进行修改，而不会给b新生成一个变量。类Man以及类Man
#的所有对象都公用这一个lis



#对象a试图修改一个属于类的 immutable的变量，则python会在内存中为对象a
#新建一个gender变量，此时a就具有了属于自己的gender变量
"""
s1 = student("zhongkang")
print(s1.name)
print(s1.age)
s1.hobits.append("basketball")
print("s1 hobits :",s1.hobits)
s1.age +=2
print(s1.age)
s2 = student("herman")

s2.favor = "game"
print(s2.favor)  #给对象a定义一个变量，对象b和类Man中都不会出现（解释性语言好随性。。）
print(" s2 hobits :",s2.hobits)
print(s2.age)
print(s2.__dict__)
print(s2.__doc__)

s1.show("hello i am kiko!")


print(hash(s2))
print(hash(s1))