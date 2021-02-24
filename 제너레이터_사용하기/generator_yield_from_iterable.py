def num_generator():
    x = [1,2,3]
    yield from x

for i in num_generator():
    print(i)