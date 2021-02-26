class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hi'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.study = 'study'

james = Student()
print(james.hello)
print(james.study)
