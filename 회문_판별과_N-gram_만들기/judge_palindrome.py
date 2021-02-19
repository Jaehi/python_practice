with open('words.txt','r') as file :
    words = file.readlines()
    for i in words:
        a = i.strip('\n')
        
        if a == a[::-1]:
            print(a)
        
        