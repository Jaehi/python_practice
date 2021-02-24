class Mogu:
    def __init__(self,stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

for i in Mogu(3):
    print(i, end=' ')

a,b,c = Mogu(3)
print(a,b,c)
