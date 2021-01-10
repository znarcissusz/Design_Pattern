class Singleton:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self,a):
        self.a = a

class Singleton2(object):
    instance = None
    def __new__(cls,*args,**kwargs):
        if cls.instance is None: #only distribute room for fist object.
            cls.instance = super().__new__(cls)
        return cls.instance

a = MyClass(10)
b = MyClass(20)

print(a.a)
print(b.a)
print(id(a),id(b))
print('-----------------------')
test1 = Singleton2()
print(test1)
test2 =Singleton2()
print(test2)
