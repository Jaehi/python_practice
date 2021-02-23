class Person:
    def greeting(self):
        print('hello')

class Student(Person):
    def greeting(self):
        print('hii')

james = Student()
james.greeting()