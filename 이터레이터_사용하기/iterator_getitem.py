class Mogu:
    def __init__(self,stop):
        self.stop = stop

    def __getitem__(self,index):
        if index < self.stop:
            return index
        else:
            raise IndexError

print(Mogu(10)[11],Mogu(3)[1],Mogu(3)[2])

for i in Mogu(3):
    print(i, end=" ")

        
