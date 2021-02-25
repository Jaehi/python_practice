
def type_check(type1,type2):
    def decorator(func):
        def wrapper(a,b):
            if isinstance(a, type1) and isinstance(b, type2):
                return func(a,b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다')
        return wrapper
    return decorator


@type_check(int,int)
def add(a,b):
    return a+b

print(add(1,2))
print(add('dd','aa'))

            

            
