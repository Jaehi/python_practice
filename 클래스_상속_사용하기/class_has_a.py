class Person:
    def greeting(self):
        print('hi')

class PersonList:
    def __init__(self):
        self.personlist = []
    
    def append_person(self, person):
        self.personlist.append(person)