from functools import wraps

class dog():
    # def __init__(self,name:'name'):
    #     self.name = name

    @staticmethod
    def safe(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self,*args,**kwargs)
            print('wrapper')
        return wrapper

class bird(dog):

    @dog.safe
    def show(self):
        print('hello')
class horse(bird):
    @bird.safe
    def talk(self):
        print('haha')

h = horse()

h.talk()
b = bird()
b.show()










