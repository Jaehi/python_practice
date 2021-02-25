def find(a):
    t = True
    while True:
        b = (yield t)
        t = a in b


f = find('Python')
next(f)

print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))
 
f.close()
