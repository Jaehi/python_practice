>>> #리스트와 튜플 사용하기
>>> 
>>> #리스트 만들기
>>> a = [1,2,3,4,5,6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> 
>>> #리스트에 여러가지 자료형 저장하기
>>> Person['Jaehi',20,165,False]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Person' is not defined
>>> person = ['JaeHi',20,165,False]
>>> person
['JaeHi', 20, 165, False]
>>> 
>>> #빈 리스트 만들기
>>> a = []
>>> a
[]
>>> b = list()
>>> b
[]
>>> 
>>> #range를 사용하여 리스트 만들기
>>> range(10)
range(0, 10)
>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = list(range(5:12))
  File "<stdin>", line 1
    b = list(range(5:12))
                    ^
SyntaxError: invalid syntax
>>> b = list(range(5,12))
>>> b
[5, 6, 7, 8, 9, 10, 11]
>>> c = list(range(1,10,2))
>>> c
[1, 3, 5, 7, 9]
>>> d = list(range(12,-10,3))
>>> d
[]
>>> d = list(range(12,,-3))
  File "<stdin>", line 1
    d = list(range(12,,-3))
                      ^
SyntaxError: invalid syntax
>>> d = list(range(12,0,-3))
>>> d
[12, 9, 6, 3]
>>> 
>>> #튜플 사용하기
>>> q = (13,24,35,46,57,68)
>>> q
(13, 24, 35, 46, 57, 68)
>>> q = 13,24,35,46,57,68
>>> q
(13, 24, 35, 46, 57, 68)
>>> person = ('jaehi',20,165,False)
>>> person
('jaehi', 20, 165, False)
>>> 
>>> #요소가 한 개 있는 튜플 만들기
>>> (4)
4
>>> (4,)
(4,)
>>> (,4)
  File "<stdin>", line 1
    (,4)
     ^
SyntaxError: invalid syntax
>>> 4,
(4,)
>>> q = tuple(range(10))
>>> q
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> w = tuple(range(1,20))
>>> w
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> e = tuple(range(-8,10,2))
>>> e
(-8, -6, -4, -2, 0, 2, 4, 6, 8)
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> b = tuple(a)
>>> b
(1, 2, 3)
>>> type
<class 'type'>
>>> type(b)
<class 'tuple'>
>>> b = (4,5,6)
>>> type(b)
<class 'tuple'>
>>> a = list(b)
>>> a
[4, 5, 6]
>>> 
>>> #list,tuple안에 문자열 넣기
>>> c = tuple('hehetkong')
>>> v = list('dehehet')
>>> c
('h', 'e', 'h', 'e', 't', 'k', 'o', 'n', 'g')
>>> v
['d', 'e', 'h', 'e', 'h', 'e', 't']
>>> 
>>> #list 와tuple로 변수 만들기
>>> a,b,c = [1,2,3]
>>> print(a,b,c)
1 2 3
>>> d,e,f = (4,5,6)
>>> print(d,e,f)
4 5 6
>>> x = [11,22,33,44]
>>> y,u,i,o = x
>>> print(y,u,i,o)
11 22 33 44
>>> y = (12,23,34,45,67,78)
>>> q,w,e,r,t,y = y
>>> print(q,w,e,r,t,y)
12 23 34 45 67 78
>>> 
>>> 
>>> #연습문제: range로 리스트 만들기
>>> a = list(range(5,-10,-2))
>>> print(a)
[5, 3, 1, -1, -3, -5, -7, -9]
>>> 
>>> #심사문제: range로 tuple만들
>>> a = int(input().split())
5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> a = int(input())
4
>>> b = tuple(range(-10,10,a))
>>> print(b)
(-10, -6, -2, 2, 6)
