jeongjaehuiui-MacBookPro:python_practice jungjaehi$ python3
Python 3.8.7 (v3.8.7:6503f05dd5, Dec 21 2020, 12:45:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 888>9
True
>>> 333<2
False
>>> 100 == 100
True
>>> 100 == "100"
False
>>> 5 != 5
False
>>> 5 == 5
True
>>> 'monmon' == "monmon"
True
>>> 'nomnom' != 'nomnom'
False
>>> 100 is "100"
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> 1 is 2
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> 100 is not "100"
<stdin>:1: SyntaxWarning: "is not" with a literal. Did you mean "!="?
True
>>> 1 == 1
True
>>> 1 == 1.0
True
>>> 1 is 1.0
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> id
<built-in function id>
>>> id(2)
4342905568
>>> id(2.0)
4347572880
>>> a = 5
>>> a is 5
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
>>> a = 6
>>> a is 6
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
>>> not False and True or not True
True
>>> 10 == 10 != 5
True
>>> 5 == 4 and !=4
  File "<stdin>", line 1
    5 == 4 and !=4
               ^
SyntaxError: invalid syntax
>>> korean = 90
>>> math = 99
>>> art = 30
>>> english = 87
>>> music = 97
>>> print(korean > 50 and math > 50 and art > 50 and english > 50 and music > 50)
False
>>> 
