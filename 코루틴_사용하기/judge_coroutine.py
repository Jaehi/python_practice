def calc():
    result = None
    while True:
        number = (yield result)
        a, b, d = number.split(' ')
        if b == '+':
            what = int(a) + int(d)
        elif b == '-':
            what = int(a) - int(d)
        elif b == '*':
            what = int(a) * int(d)
        elif b == '/':
            what = '{:.1f}'.format(float(a) / float(d))

        
expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()

