"""

implement a queue with two stack

implement function [push,pop,len]

"""

class stack():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()


# s1 = stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# a=s1.pop()
# print(a)
#print(s1.size())

# while s1.items:
#     print("while ",s1.pop())

class queque():
    def __init__(self):
        self.push_stack = stack()
        self.pop_stack  = stack()
    def push(self,item):
        if self.pop_stack.items and not self.push_stack.items:
            self.convert(self.pop_stack,self.push_stack)
            self.push_stack.items.append(item)
        else:
            self.push_stack.items.append(item)

    def pop(self):
        if self.push_stack.items and not self.pop_stack.items:
            self.convert(self.push_stack,self.pop_stack)
            return self.pop_stack.items.pop()
        else:
            self.pop_stack.items.pop()

    def convert(self,s1,s2):
        while s1.items:
            s2.items.append(s1.items.pop())

q1 = queque()
q1.push(1)
q1.push(2)
q1.push(3)
q1.push(4)

print("queque pop items",q1.pop_stack.items)
print("queque push items ",q1.push_stack.items)

print("pop ",q1.pop())

