import functools

def is_multiple(x):
    def decorator(func):
        @functools.wraps(func)
        def wrraper(a,b):
            r = func(a,b)
            if r % x == 0:
                print(f'{func.__name__}의 반환값은 {x}의 배수가 맞습니다')
            else:
                print(f'{func.__name__}의 반환값은 {x}의 배수가 아닙니다')
            return r
        return wrraper
    return decorator

@is_multiple(3)
@is_multiple(7)
def add(a,b):
    return a+b

print(add(10,20))