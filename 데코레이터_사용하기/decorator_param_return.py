def decorator(func):
    def wrapper(a,b):
        r = func(a,b)
        print('{0}(a = {1}, b = {2}) -> {3}'.format(func.__name__,a,b,r))
        return r
    return wrapper

@decorator
def add(a,b):
    return a + b

a = add(1,2)
print(a)