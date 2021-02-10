>>> #출력 방법 알아보기
>>> #값을 여러개 출력하기
>>> print(4,5,6)
4 5 6
>>> print('sss','ppp')
sss ppp
>>> 
>>> #sep로 값 사이에 문자넣기
>>> print('안녕','나는','어쩌구라고해','잘부탁해', sep = '.....')
안녕.....나는.....어쩌구라고해.....잘부탁해
>>> 
>>> #줄바꿈 활용하기
>>> print(1,23,4)
1 23 4
>>> print(1,23,4,sep"\n")
  File "<stdin>", line 1
    print(1,23,4,sep"\n")
                    ^
SyntaxError: invalid syntax
>>> print(1,23,4,sep="\n")
1
23
4
>>> print('1\n23\n4')
1
23
4
>>> print(1,2,3,4, sep="\t")
1	2	3	4
>>> print(1,2,3,4 , sep="\\"
... )
1\2\3\4
>>> 
>>> #end 사용하기
>>> print(1)
1
>>> print(2)
2
>>> print(1);print(2);print(3)
1
2
3
>>> print(1,end="");print(2,end='');print(3)
123
>>> print(1,end=" ");print(2,end="222222");print(3)
1 22222223
>>> #연습문제: 날짜와 시간 출력하기
>>> year = 2000
>>> month = 10
>>> day = 27
>>> hour = 11
>>> minute = 43
>>> second = 59
>>> print(year,month,day,sep="//");print(hour,minute,second,sep=":")
2000//10//27
11:43:59
>>> #\랑 헷갈렷네요
>>> 
>>> print(year,month,day,sep="/",end=" ");print(hour,minute,second,sep=":")
2000/10/27 11:43:59
>>> 
