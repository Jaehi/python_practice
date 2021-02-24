class MultipleIterator:
    def __init__(self, stop, multiple):
        self.bass = 0
        self.stop = stop
        self.multiple = multiple
               
 
    def __iter__(self):
        return self
 
    def __next__(self):
        self.bass += 1
        if self.multiple * self.bass < self.stop:
            return self.multiple * self.bass
        else:
            raise StopIteration
               
 
for i in MultipleIterator(20, 3):
    print(i, end=' ')
 
print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')