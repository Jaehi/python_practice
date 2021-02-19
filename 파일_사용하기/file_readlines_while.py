with open('hello.txt','r') as file:
    fruits = None
    while fruits != "":
        fruits = file.readline()
        print(fruits.strip('\n'))
