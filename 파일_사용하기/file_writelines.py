fruits = ['watermelon\n','peach\n','banana\n','apple\n','orange\n']
with open('hello.txt','w') as file:
    file.writelines(fruits)