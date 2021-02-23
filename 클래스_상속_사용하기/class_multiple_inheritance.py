class Person:
    def greeting(self):
        print('안녕하세요')

class Universitiy:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person,Universitiy):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()