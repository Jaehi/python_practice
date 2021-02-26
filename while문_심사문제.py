>>> i = 2
>>> j = 5
>>> while i <= 32 or j >= 1:
...     i = i*2
...     j = j-1
...     print(i,j)
... 
4 4
8 3
16 2
32 1
64 0
>>> while i <= 32 or j >= 1:
...     print(i,j)
... while i <= 32 or j >= 1:
KeyboardInterrupt
>>> i = 2
>>> j = 5
>>> while i <= 32 or j >= 1:
...     print(i,j)
...     i = i*2
...     j = j-1
... 
2 5
4 4
8 3
16 2
32 1
>>> 
>>> #심사문제: 교통카드 잔액 출력하기
>>> money = int(input())
15000
>>> while money > 1350 :
...     money = money - 1350
...     print(money)
... 
13650
12300
10950
9600
8250
6900
5550
4200
2850
1500
150
>>> 



word = input('단어를 입력하세요 : ')
is_palindrome = True
for i in range(len(word)//2):
    if word[i] != word[-1 -i]:
        is_palindrome = False
        break
print(is_palindrome)
    