with open('words.txt','r') as file:
    count = 0
    words = file.readlines()

    for i in words:
        if len(i.strip('\n')) <= 10:
            count += 1

    print(count)