>>> #불과 논리 연산자 알아보기
>>> # +비교
>>> 
>>> #불과 비교 연산자 사용하기
>>> True
True
>>> False
False
>>> 
>>> #비교 연산자의 판단 결과
>>> 3 > 1
True
>>> 1 > 3
False
>>> 
>>> #숫자가 같은지 다른지 비교하기
>>> 10 == 10
True
>>> 1== 9
False
>>> 1 != 9
True
>>> 
>>> #문자열이 같은지 다른지 비교하기
>>> 'hi' == "hi"
True
>>> 'Hi' == 'hi'
False
>>> 'Hi' != 'hi'
True
>>> 
>>> #부등호 사용하기
>>> 10 > 20
False
>>> 10 < 20
True
>>> 10 <=10
True
>>> 
>>> #객체가 같은지 다른지 비교하기
>>> 1 is 1.0
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> 1 == 1.0
True
>>> 1 is not 1.0
<stdin>:1: SyntaxWarning: "is not" with a literal. Did you mean "!="?
True
>>> "hi" is 'hi'
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
>>> 
>>> #메모리 주소 구하기
>>> id(a)
4403447040
>>> id(1)
4403444416
>>> id(1.0)
4414701968
>>> 
>>> 
>>> #논리 연산자 사용하기
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> 
>>> True or True
True
>>> True or False
True
>>> False or Flase
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Flase' is not defined
>>> False or False
False
>>> 
>>> not True
False
>>> not False
True
>>> not True and False or not False
True
>>> 
>>> #논리 연산자와 비교 연산자 같이 사용하
>>> 10 == 10 and 10 != 5
True
>>> 4 == 5 and 3 == 3
False
>>> 10 > 5 or 9 < 3
True
>>> not 3 > 6
True
>>> 1 is not 1.0
<stdin>:1: SyntaxWarning: "is not" with a literal. Did you mean "!="?
True
>>> bool(1)
True
>>> bool(1.2)
True
>>> bool(0)
False
>>> bool('we')
True
>>> bool("")
False
>>> 
>>> #단락 평가
>>> 
>>> print(True or False)
True
>>> print(False or False)
False
>>> print('hh' or 'tt')
hh
>>> print('ee' and 're')
re
>>> print(False or 'ee')
ee
>>> 
>>> #연습문제: 합격 여부 출력하기
>>> korean = 92
>>> english = 47
>>> mathematics = 86
>>> science = 81
>>> print(50>korean and 50>english and 50>mathmatics and 50>science)
False
>>> 
>>> #심사문제 : 합격 여부 출력하기
>>> korean,english,math,science = map(int,input().split())
90 81 86 80
>>> print(korean >= 90 and english > 80 and math > 85 and science >=80)
True
>>> 
