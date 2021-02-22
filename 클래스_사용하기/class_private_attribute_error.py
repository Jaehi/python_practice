class Person:
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

maria = Person('maria',22,'서울시 서초구 반포동',5000)
maria.__wallet -= 100

