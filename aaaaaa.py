def prime_number_generator(start,stop):
    for i in range(start,stop):
        for n in range(2, i):
            is_prime = True
            if i % n != 0:
                n
            else:
                is_prime = False
        yield is
    
                

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')