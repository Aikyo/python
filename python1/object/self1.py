class student:
    age = 0
    name = "beibei"
    def __init__(self):
        self.school = "zhongxue"
    def count(self):
        self.name = "feifei"

s1 = student()
s1.count()
print(s1.school)
print("s1 name",s1.name)
print("s1 age :",s1.age)
s1.age = 13
print("s1 age :",s1.age)
print()


s2 = student()
print("s2 name",s2.name)
print(s2.school)
print("s2 age :",s2.age)



