class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

class Student(Person):
    pass

james = Student()
print(james.hello)