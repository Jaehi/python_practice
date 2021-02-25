def decorator(func):
    def wrapper(self,a,b):
        self.a = a
        self.b = b
        r = func(self,a,b)
        print('{0}(a = {1}, b = {2}) -> {3}'.format(func.__name__, a, b,r))
        return r
    return wrapper

class Calc:
    @decorator
    def add(self,a,b):
        return a+b

    @decorator
    def mul(self,a,b):
        return a*b

c = Calc()
print(c.add(1,2))
print(c.mul(6,8))


    
