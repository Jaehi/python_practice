# fruits = ['watermelon\n','peach\n','banana\n','apple\n','orange\n']
with open('hello.txt','r') as file:
    fruits = file.readlines()
    print(fruits)