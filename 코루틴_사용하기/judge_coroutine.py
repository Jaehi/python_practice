def calc():
    a = None
    while True:
        expression = (yield a)
        a, b, d = expression.split(' ')
        if b == '+':
            a = int(a) + int(d)
        elif b == '-':
            a = int(a) - int(d)
        elif b == '*':
            a = int(a) * int(d)
        elif b == '/':
            a = '{:.1f}'.format(float(a) / float(d))
        
expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()

