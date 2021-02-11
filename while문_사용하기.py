>>># while문 사용하기
>>> i = 0
>>> while i < 10:
...     print('good')
...     i += 1
... 
good
good
good
good
good
good
good
good
good
good
>>> 
>>> # 초깃값을 1부터 시작하기
>>> i = 1 
>>> while i < 10:
...     print('goood')
...     i += 1
... 
goood
goood
goood
goood
goood
goood
goood
goood
goood
>>> while i < 10:
...     print(i)
...     i += 1
... 
>>> i = 1
>>> while i < 10:
...     pr
KeyboardInterrupt
>>> while i < 10:
...     print(i)
...     i += 1
... 
1
2
3
4
5
6
7
8
9
>>> #초깃값을 감소시키기
>>> i = 10
>>> while i > 0:
...     print(i)
...     i -= 1
... 
10
9
8
7
6
5
4
3
2
1
>>> 
>>> #입력한 횟수대로 반복하기
>>> count = int(input())
5
>>> while count > 0:
...     print(count)
...     count -= 1
... 
5
4
3
2
1
>>> import random
>>> i = 0
>>> while i != 5:
...     i = random.randint(1,10)
...     print(i)
... 
2
6
4
8
2
7
10
6
1
7
6
8
6
6
4
7
9
1
8
1
1
3
7
1
5
>>> 
>>> #시퀀스 객체에서 요소를 무작위로 선택하기
>>> dice = [1,2,3,4,5,6]
>>> i = 0
>>> while i != 2:
...     i = random.choice(dice)
...     print(i)
... 
3
3
1
2
>>> 
