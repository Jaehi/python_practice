class Person:
    bag = []
    def __init__(self):
        self.bag = []
    def put_bag(self,stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('안경')

maria = Person()
maria.put_bag('치약')

print('{}\n{}'.format(james.bag,maria.bag))