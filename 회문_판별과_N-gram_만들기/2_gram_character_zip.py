text = 'today'
gram = list(zip(text , text[1:]))
print(gram)
for i in gram:
    print(i[0],i[1],sep = '')