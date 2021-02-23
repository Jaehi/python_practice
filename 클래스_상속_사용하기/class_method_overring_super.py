class Person:
    def gretting(self):
        print('hello')

class Student(Person):
    def gretting(self):
        super().gretting()
        print('hi')

james = Student()
james.gretting()