class IsMultiple:
    def __init__(self,x):
        self.x = x
    def __call__(self,func):
        def wrapper(a,b):
            r = func(a,b)
            if r % self.x == 0:
                print(f'{func.__name__}의 반환값은 {self.x}의 배수가 맞습니다')
            else:
                print(f'{func.__name__}의 반환값은 {self.x}의 배수가 아닙니다')
            return r
        return wrapper

@IsMultiple(5)
def add(a,b):
    return a+b

print(add(10,20))