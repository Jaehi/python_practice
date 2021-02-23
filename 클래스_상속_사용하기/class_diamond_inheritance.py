class A:
    def greeting(self):
        print('A')

class B(A):
    def greeting(self):
        print('B')

class C(A):
    def greeting(self):
        print('C')
    
class D(B,C):
    pass

asdf = B()
asdf.greeting()