def one_generator():
    yield 1
    return 'return에 저장된 값'

try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)