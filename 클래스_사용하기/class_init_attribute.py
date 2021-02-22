class Person:
    def __init__(self,name,age,address):
        self.talk = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0}, 저는 {1}입니다, 나이는 {2}살 이고 {3}에 거주중 입니다'.format(self.talk,self.name,self.age,self.address))

maria = Person('maria','22','서울시 서초구 반포동')
maria.greeting()