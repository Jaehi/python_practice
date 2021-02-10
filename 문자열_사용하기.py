>>> #문자열 사용하기 
>>> hey = "hey"
>>> hey
'hey'
>>> hi = """hi"""
>>> hi
'hi'
>>> a = """qqq
... www
... eee
... rrr"""
>>> a
'qqq\nwww\neee\nrrr'
>>> print(a)
qqq
www
eee
rrr
>>> an = "isisisis isn't "
>>> an
"isisisis isn't "
>>> na = 'i can "no"'
>>> na
'i can "no"'
>>> some = """"내"가 
... 바로
... '쿠키'
... 다"""
>>> some
'"내"가\n바로\n\'쿠키\'\n다'
>>> print(some)
"내"가
바로
'쿠키'
다
>>> 
>>> #문자열에 따옴표를 추가하는 다른 방법
>>> 'i can\'t do this'
"i can't do this"
>>> print(real\nreal\nreal)
  File "<stdin>", line 1
    print(real\nreal\nreal)
                          ^
SyntaxError: unexpected character after line continuation character
>>> print('real\nreal\nreal\n)
  File "<stdin>", line 1
    print('real\nreal\nreal\n)
                             ^
SyntaxError: EOL while scanning string literal
>>> print('real\nreal\nreal\n')
real
real
real

>>> #연습문제: 여러 줄로 된 문자열 사용하기
>>> 
>>> s = '''Python is a programming language that lets you work quickly
... and
... integrate systems more effectively.'''
>>> print(s)
Python is a programming language that lets you work quickly
and
integrate systems more effectively.
>>> 
>>> #심사문제: 여러 줄로 된 문자열 사용하기
>>> s = """'Python' is a "programming language"
... that lets you work quickly
... and
... integrate systems more effectively."""
>>> print(s)
'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.
