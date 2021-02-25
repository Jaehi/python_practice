def decorator(func):
    def wrapper(*args,**kwargs):
        r = func(*args,**kwargs)
        print('{0}(args = {1}, kwargs = {2}) -> {3} '.format(func.__name__,args,kwargs,r))
        return r
    return wrapper

@decorator
def get_max(*args):
    return max(args)

@decorator
def get_min(**kwargs):
    return min(kwargs.values())
@decorator
def add(a,b):
    return a + b

print(get_max(10,20))
print(get_min(a = 10, b = 20, c = 30))
print(add(10,20))
print(add(a= 10 , b = 20))