def prime_number_generator(start,stop):

    for i in range(start,stop):
        what=True
        
        for j in range(2,i-1):
            if i%j==0:
                what=False
        if what==True:
            yield i


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')