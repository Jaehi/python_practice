>>> #중첩 루프 사용하기
>>> for i in range(5):
...     for j in range(5):
...             print('j:', j, sep='', end=' ') 
...     pront('i:',i,'\\n',sep='')
... 
KeyboardInterrupt
>>> for i in range(5):
...     for j in range(5):
...             print('j:', j, sep='', end=' ') 
...     print('i:',i,'\\n',sep='')
... 
j:0 j:1 j:2 j:3 j:4 i:0\n
j:0 j:1 j:2 j:3 j:4 i:1\n
j:0 j:1 j:2 j:3 j:4 i:2\n
j:0 j:1 j:2 j:3 j:4 i:3\n
j:0 j:1 j:2 j:3 j:4 i:4\n
>>> 
>>> #사각형으로 별 출력하기
>>> for i in range(5):
...     for j in range(5):
...             print('*',end="")
...     print()
... 
*****
*****
*****
*****
*****
>>> for i in range(3):
...     for j in range(7):
...             print('*',end = " ")
...     print()
... 
* * * * * * * 
* * * * * * * 
* * * * * * * 
>>> #계단식으로 별 출력하기
>>> for i in range(5):
...     for j in range(5):
...             if j <= i:
...                     print('*',end = "")
...     print()
... 
*
**
***
****
*****
>>> #대각선으로 별 출력하기
>>> for i in range(5):
...     for j in range(5):
...             if j == 1:
...                     print('*',end = "")
...     print()
... 
*
*
*
*
*
>>> #대각선으로 별 출력하기
>>> for i in range(5):
...     for j in range(5):
...             if j == i:
...                     print('*',end = "")
...             else:
...                     print(' ', end = "")
...     print()
... 
*    
 *   
  *  
   * 
    *
>>> 
>>> #연습문제: 역삼각형 모양으로 별 출력하기
>>> for i in range(5):
...     for i in range(5):
...             if j < i:
...                     print(' ',end="")
...             else:
...                     print('*',end="")
...     print()
... 
*****
*****
*****
*****
*****
>>> for i in range(5):
...     for j in range(5):
...             if j < i:
...                     print(' ',end = "")
...             else:
...                     print('*',end="")
...     print()
... 
*****
 ****
  ***
   **
    *
