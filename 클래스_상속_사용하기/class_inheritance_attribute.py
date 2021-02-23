class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.study = 'study'

james = Student()
print(james.hello, james.study)