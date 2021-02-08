>>> print(1,2,3)
1 2 3
>>> print("Hi","I'm","Jaehi",sep="_"
... _
  File "<stdin>", line 2
    _
    ^
SyntaxError: invalid syntax
>>> print("Hi","I'm","Jaehi",sep="_")
Hi_I'm_Jaehi
>>> print(4,5,6,end="88")
4 5 688>>> 
>>> print("heeelllllooo","hhhhhiiiii",sep="\n")
heeelllllooo
hhhhhiiiii
>>> print("hello\nhi")
hello
hi
>>> print("qwer\trewq)
  File "<stdin>", line 1
    print("qwer\trewq)
                     ^
SyntaxError: EOL while scanning string literal
>>> print("qwer\trewq")
qwer	rewq
>>> year = 2000
>>> month = 10
>>> day = 27
>>> hour = 11
>>> minute = 43
>>> second = 59
>>> print(year,month,day,sep="/",end="")
2000/10/27>>> print(hour,minute,second,sep=":")
11:43:59
>>> print(year,month,day,sep="-",end="t")
2000-10-27t>>> print(year,month,day,sep="-",end="t")print(hour,minute,second,sep=":")
  File "<stdin>", line 1
    print(year,month,day,sep="-",end="t")print(hour,minute,second,sep=":")
                                         ^
SyntaxError: invalid syntax
>>> 
