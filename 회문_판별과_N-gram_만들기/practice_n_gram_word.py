count = int(input())
text = input()
word = text.split()

if len(word) < count:
    print('wrong')
else:
    n_gram = zip(*[word[i:] for i in range(count)])

    for i in n_gram:
        print(i)
    
