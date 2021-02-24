def num_generator(stop):
    n = 0
    while n < stop:
        yield  n
        n += 1

def three_generator():
    yield from num_generator(3)
 
for i in three_generator():
    print(i)