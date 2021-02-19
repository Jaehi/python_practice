with open('hello.txt','r') as file:
    for fruits in file:
        print(fruits.strip('\n'))