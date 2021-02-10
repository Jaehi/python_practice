>>> #시퀀스 자료형 활용하기
>>> 
>>> #특정 값이 있는지 확인하기
>>> a = [0,10,20,30,40,50,60,70,80,90]
>>> 30 in a
True
>>> 100 in a
False
>>> 100 not in a
True
>>> 30 not in a
False
>>> 
>>> 12 in (1,2,3,4,11,12)
True
>>> 5 in range(10)
True
>>> 'P' in 'Cookie'
False
>>> 
>>> #시퀀스 객체 연결하기
>>> a = [0,10,20,30]
>>> b = [9,8,7,6]
>>> a+b
[0, 10, 20, 30, 9, 8, 7, 6]
>>> 
>>> #range는 + 연산자로 객체를 연결할 수 없다
>>> range(0,10) + range(10,20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'range' and 'range'
>>> 
>>> list(range(0,10))+list(range(50,90))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
>>> tuple(range(1,5))+tuple(range(3,9))
(1, 2, 3, 4, 3, 4, 5, 6, 7, 8)
>>> 'Hi'+'Cookies'
'HiCookies'
>>> 'Hi'+127
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'Hi'+str(127)
'Hi127'
>>> 
>>> #시퀀스 객체 반복하기
>>> [1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
>>> #range는 *연산자로 반복도 못한다
>>> range(0,5,2)*100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'range' and 'int'
>>> 
>>> list(range(0,5,2))*10
[0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4]
>>> tuple(range(0,5,1))*5
(0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4)
>>> 'No   '*10
'No   No   No   No   No   No   No   No   No   No   '
>>> 
>>> #시퀀스 객체의 요소 개수 구하기
>>> a[1,2,3,4,5,6,7,8,9,99]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> a = [1,2,3,4,5,6,7,8,9,99]
>>> len(a)
10
>>> b = (1,2,3,4,5)
>>> len(a)
10
>>> len(b)
5
>>> len(range(0,100,1))
100
>>> 
>>> #문자열 길이 구하기
>>> hi = 'hiiihihihiihihi'
>>> len(hi)
15
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
>>> a[1]
2
>>> a[9]
99
>>> # 위에꺼부터 인덱스 사용하기 
>>> b = (1,23,4,5,6,78)
>>> b[0]
1
>>> range = range(0,500,2)
>>> range[400]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: range object index out of range
>>> range[100]
200
>>> 
>>> #getitem 메소드
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
>>> a.__getitem__(3)
4
>>> 
>>> #음수 인덱스 지정하기
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
>>> 
>>> a[-1]
99
>>> a[-3]
8
>>> b 
(1, 23, 4, 5, 6, 78)
>>> b[-1]
78
>>> b[-4]
4
>>> range[-150]
200
>>> range[-100]
300
>>> hi
'hiiihihihiihihi'
>>> hi[5]
'i'
>>> 
>>> #인덱스의 범위를 벗어나면
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
>>> a[11]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> 
>>> #마지막 요소에 접근하기
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
>>> len(a)
10
>>> a[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> a[9]
99
>>> a[len(a)-1]
99
>>> #저번에 len그냥 썼다가 오류났는데 index을 구할땐 -1 해줘야한다
>>> 
>>> #요소에 값 할당하기
>>> a = [0,0,0,0,0,0]
>>> a[0] = 1
>>> a[1] = 2
>>> a[2] = 3
>>> a[3] =4
>>> a[4] = 5
>>> a[5] = 6
>>> a
[1, 2, 3, 4, 5, 6]
>>> a[0]
1
>>> 
>>> #튜플은 값을 저장할 수 없다 값을 바꿀수 없어서 오류남
>>> b tuple(0,0,0,0)
  File "<stdin>", line 1
    b tuple(0,0,0,0)
      ^
SyntaxError: invalid syntax
>>> b = tuple(0,0,0,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tuple expected at most 1 argument, got 4
>>> b = (0,0,0,0)
>>> b[0] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> #range는 역시 안된다
>>> r
45
>>> range
range(0, 500, 2)
>>> range[5] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object does not support item assignment
>>>  
>>> #그런데 이제 문자열도 바꿀수 없다
>>> hi
'hiiihihihiihihi'
>>> hi[4] = 'K'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
>>> #del로 요소 삭제하
>>> a
[1, 2, 3, 4, 5, 6]
>>> del a[4]
>>> a
[1, 2, 3, 4, 6]
>>> b
(0, 0, 0, 0)
>>> del b[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
>>> #튜플은 역시 삭제할 수 없다
>>> 
>>> #range도 문자열도 마찬가지,,
>>> 
>>> 
>>> #슬라이스 사용하기
>>> a = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,100]
>>> a[0:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> #끝 인덱스는 가져오려는 것 보다 1 더 크게 지정해야 한다
>>> len(a)
20
>>> a[0:len(a)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> a[11:19]
[12, 13, 14, 15, 16, 17, 18, 19]
>>> 
>>> a[10:-1]
[11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> a[1:3:3]
[1]
>>> a[1:19:3]
[1, 4, 7, 11, 14, 17]
>>> a[0:21]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> 
>>> #인덱스 생략하기
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> a[:9]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> a[1:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> a[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> 
>>> 
>>> #인덱스 생략하면서 증가폭 사용하기
>>> a[:19:2]
[0, 2, 4, 6, 8, 11, 13, 15, 17, 19]
>>> a[1::3]
[1, 4, 7, 11, 14, 17, 100]
>>> a[::4]
[0, 4, 8, 13, 17]
>>> a[::]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> 
>>> #슬라이스 인덱스 증가폭을 음수로 지정하면 요소를 뒤에서 부터 가져온다
>>> a[5:1:-1]
[5, 4, 3, 2]
>>> a[::-1]
[100, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> #len응용하기
>>> a[0:len(a)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> 
>>> #튜플,range,문자열에 슬라이스 사용하기
>>> b = (1,2,3,4,5,6,7,8,9)
>>> b[4:7]
(5, 6, 7)
>>> b[:len(b)]
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> b[:len(b):2
... ]
(1, 3, 5, 7, 9)
>>> range
range(0, 500, 2)
>>> range[100:144]
range(200, 288, 2)
>>> r = range(10
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object is not callable
>>> r = range(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object is not callable
>>> del range
>>> r = ranage(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ranage' is not defined
>>> range(10)
range(0, 10)
>>> r = range(10)
>>> r[3:8]
range(3, 8)
>>> r[:8:1]
range(0, 8)
>>> list(r[:8:1])
[0, 1, 2, 3, 4, 5, 6, 7]
>>> hi[3:8]
'ihihi'
>>> hi[:4:1]
'hiii'
>>> #slice 객체 사용하기
>>> range(10)[slice(2,9,2)]
range(2, 9, 2)
>>> range(10).__getitem__(slice(1,8,1))
range(1, 8)
>>> 
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> s = slice(4,7)
>>> a[s]
[4, 5, 6]
>>> r = range(10)
>>> r[s]
range(4, 7)
>>> hi[s]
'hih'
>>> 
>>> #슬라이스에 요소 할당하기
>>> a[2:8] = [21,22,23,24,25,26]
>>> a
[0, 1, 21, 22, 23, 24, 25, 26, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> a[2:9] = ['b']
>>> a
[0, 1, 'b', 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
>>> a[2:7] = ['a','c','v','d','y','h','e','o']
>>> a
[0, 1, 'a', 'c', 'v', 'd', 'y', 'h', 'e', 'o', 14, 15, 16, 17, 18, 19, 100]
>>> a
[0, 1, 'a', 'c', 'v', 'd', 'y', 'h', 'e', 'o', 14, 15, 16, 17, 18, 19, 100]
>>> a[10:15:1] = [100,200,300,400,500]
>>> a
[0, 1, 'a', 'c', 'v', 'd', 'y', 'h', 'e', 'o', 100, 200, 300, 400, 500, 19, 100]
>>> #튜플,range,문자열은 슬라이스 범위를 지정하더라도 요소를 할당할 수 없다
>>> 
>>> #del로 슬라이스 삭제하기
>>> a
[0, 1, 'a', 'c', 'v', 'd', 'y', 'h', 'e', 'o', 100, 200, 300, 400, 500, 19, 100]
>>> del a[0:10]
>>> a
[100, 200, 300, 400, 500, 19, 100]
>>> a[1]
200
>>> del a[1:3:1]
>>> a
[100, 400, 500, 19, 100]
>>> 
>>> #연습문제: 최근 3년간 인구 출력하기
>>> year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
>>> population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
>>> print(year[-3:])
[2016, 2017, 2018]
>>> print(population[-3:]
... )
[9930616, 9857426, 9838892]
>>> 
>>> #연습문제: 인덱스가 홀수인 요소 출력하기
>>> 
>>> n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
>>> print(1:len(n):2)
  File "<stdin>", line 1
    print(1:len(n):2)
           ^
SyntaxError: invalid syntax
>>> print(n[1:len(n):2])
(75, -10, 32, -15, 76, 2)
>>> 
>>> #심사문제: 리스트 마지막 부분 삭제하기
>>> x = input().split()
1 2 3 4 5 6 7 8 9 10
>>> a = list(x)
>>> del a[-5:]
>>> b = tuple(a)
>>> print(b)
('1', '2', '3', '4', '5')
>>> 
>>> #심사문제: 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
>>> ghf,wkr = input().split()
qwer
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 2, got 1)
>>> ghf,wkr = input().split()
qwertyui asdfghj
>>> ghff = list(ghf)
>>> wkrr = list(wkrr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wkrr' is not defined
>>> wkrr = list(wkr)
>>> print(ghff[:len(ghff):2]+wkrr[1:len(wkrr):2])
['q', 'e', 't', 'u', 's', 'f', 'h']
