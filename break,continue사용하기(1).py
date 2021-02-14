#break, continue로 반복제어하기
>>> 
>>> #while에서 break로 반복문 끝내기
>>> i = 0
>>> while True:
...     print(i)
...     i += 1
...     if i == 10:
...             break
... 
0
1
2
3
4
5
6
7
8
9
>>> 
>>> #for문에서 break로 반복문 끝내기
>>> for j in range(100):
...     print(j)
...     if j == 10:
...             break
... 
0
1
2
3
4
5
6
7
8
9
10
>>> 
>>> # for에서 continue로 실행코드 건너뛰기
>>> for j in range(20):
...     if i % 2 == 0:
...             continue
...     print(j)
... 
>>> 
>>> for k in range(20):
...     if k % 2 == 0:
...             break
...     print(k)
... 
>>> for k in range(20):
...     if k % 2 == 0:
...             continue
...     print(k)
... 
1
3
5
7
9
11
13
15
17
19
>>> 
>>> #while 반복문에서 continue로 실행코드 건너 뛰기
>>> i = 0
>>> while i < 20:
...     i += 1
...     print(i)
...     if i % 2 == 0:
...             continue
  File "<stdin>", line 4
    if i % 2 == 0:
                 ^
IndentationError: expected an indented block
>>> i = 0
>>> while i < 20:
...     i += 1
...     if i % 2 == 0:
...             continue
...     print(i)
... 
1
3
5
7
9
11
13
15
17
19
>>> for h in range(100):
...     pass
... 
>>> while True:
...     pass
... 

^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> 
>>> #입력한 횟수대로 반복하
>>> count = int(input())
10
>>> i = 0
>>> while True:
...     print(i)
...     i += 1
...     if i == count:
...             break
... 
0
1
2
3
4
5
6
7
8
9
>>> #입력한 숫자까지 홀수 출력하기
>>> count = int(input())
20
>>> for i in range(count):
...     i += 1
KeyboardInterrupt
>>> count
20
>>> for i in range(count + 1):
...     if i % 2 == 0:
...             continue
...     print(i)
... 
1
3
5
7
9
11
13
15
17
19
