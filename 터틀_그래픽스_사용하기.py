 import turtle as t
>>> t.shape('turtle')
>>> t.foward(100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'turtle' has no attribute 'foward'
>>> t.forward(100)
>>> 





























































 t.right(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.right(90)
>>> t.right(90)
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> for i in range(5):
...     t.forward(100)
...     t.right(360/5)
... 
>>> n = int(input())
7
>>> for i in range(n)
  File "<stdin>", line 1
    for i in range(n)
                    ^
SyntaxError: invalid syntax
>>> for i in range(n)
  File "<stdin>", line 1
    for i in range(n)
                    ^
SyntaxError: invalid syntax
>>> n
7
>>> for i in range(n):
...     t.forward(100)
...     t.right(360/n)
... 
>>> t.color('blue')
>>> t.begin_fill()
>>> for i in range(n)
  File "<stdin>", line 1
    for i in range(n)
                    ^
SyntaxError: invalid syntax
>>> for i in range(n):
...     t.forward(150)
...     t.right(360/n)
... 
>>> t.end_fill()
>>> y = 60
>>> t.speed('fastest')
>>> for i in range(n):
...     t.circle(120)
...     t.right(360/n)
... 
>>> for i in range(y):
...     t.circle(120)
...     t.right(360/n)
... 
>>> y
60
>>> for i in range(y):
...     t.circle(120)
...     t.right(360/y)
... 
>>> for i in range(300):
...     t.forward(i)
...     t.right(91)
... 
