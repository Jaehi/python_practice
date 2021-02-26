with open('judge.txt','r') as file:
    judge = file.readlines()
    print(judge)

    for i in judge:
        a = i.split()

        for j in a:
            if 'c' in j:
                print(j.strip(',.'))
        
    print()