>>> #입력 값을 변수에 저장하기
>>> #input함수 사용하기
>>> input
<built-in function input>
>>> input()
i do
'i do'
>>> 
>>> #input 함수의 값을 변수에 할당하기
>>> u = input()
우리가 함께하는
>>> u
'우리가 함께하는'
>>> u = input
>>> u = input('입력하세요 : ')
입력하세요 : 넴
>>> u
'넴'
>>> 
>>> #입력한 두 수의 합 구하기
>>> a = input(); b = input()
7
8
>>> print(a+b)
78
>>> type(a)
<class 'str'>
>>> 
>>> #입력값을 정수로 바꾸기
>>> a = int(input())
5
>>> b = int(input())
5
>>> print(a+b)
10
>>> 
>>> #입력값을 변수 두개에 입력하기
>>> a, b, c = input().split()
7 8 9
>>> print(a+b-c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> print(a+b+c)
789
>>> #두 숫자의 합
>>> q,w = int(input().split())
1 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> q,w = intput().split()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'intput' is not defined
>>> q,w = input().split()
1 2
>>> int(q)
1
>>> int(w)
2
>>> print(q+w)
12
>>> a = int(q)
>>> b = int(w)
>>> print(a+b)
3
>>> q,w = map(int,input().split(','))
4,5
>>> print(q+w)
9
>>> 
>>> #연습문제: 정수 세 개를 입력받고 합계 출력하기
>>> a,b,c = map(int,input().split())
-10 20 30
>>> print(a+b+c)
40
>>> 
>>> #심사문제: 변수 만들기
>>> a = 50
>>> b = 100
>>> c = None
>>> print(a)
50
>>> print(b)
100
>>> print(c)
None
>>> 
>>> #심사문제: 평균 점수 구하기
>>> a,b,c,d = map(int,input().split())
83 92 87 90
>>> print((a+b+c+d)//4)
88
