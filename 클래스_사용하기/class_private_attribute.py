class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    
    def pay(self, amount):
        self.__wallet -= amount
        print('이제 잔고가 {}원 남으셨습니다.'.format(self.__wallet))

maria = Person('maria',22,'서울시 서초구 반포동',10000)
maria.pay(7000)