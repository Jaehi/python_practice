def is_multiple(x):
    def decorator(func):
        def wrapper(a,b):
            r = func(a,b)
            if r % x == 0:
                print(f'{func.__name__}의 반환값은 {x}의 배수 입니다')
            else:
                print(f'{func.__name__}의 반환값은 {x}의 배수가 아닙니다')
            return r
        return wrapper
    return decorator

@is_multiple(5)
def add(a,b):
    return a+b

@is_multiple(3)
def mul(a,b):
    return a*b

print(mul(3,5))
print(add(9,3))