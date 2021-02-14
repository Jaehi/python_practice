>>> #3의 배수일 때와 5의 배수일 때 처리하기
>>> for i in range(1,51):
...     if i % 3 == 0:
...             print("Fizz")
...     elif i % 5 == 0:
...             print("Buzz")
...     else:
...             print(i)
... 
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
Fizz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
Fizz
46
47
Fizz
49
Buzz
>>> #3과 5의 공배수 처리하기
>>> for i in range(1, 51):
...     if i % 3== 0 and i % 5 ==0:
...             print("FizzBuzz")
...     elif i % 3 == 0:
...             print("Fizz")
...     elif i % 5 == 0:
...             print("Buzz")
...     else:
...             print(i)
... 
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
>>> #코드 단축하기
>>> for i in range(1, 51):
...     print("Fizz"*(i%3==0)+"Buzz"*(i%5==0)or i)
... 
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
>>> #연습문제: 2과 11의 배수, 공배수 처리하기
>>> for i in range(1, 51):
...     if i % 2 == 0 and i % 11 == 0:
...             print("FizzBuzz)
  File "<stdin>", line 3
    print("FizzBuzz)
                   ^
SyntaxError: EOL while scanning string literal
>>> for i in range(1, 51):
...     if i % 2 == 0 and i % 11 == 0:
...             print("FizzBuzz")
...     elif i % 2 == 0:
...             print("Fizz")
...     elif i % 11 == 0:
...             print("Buzz")
...     else:
...             print(i)
... 
1
Fizz
3
Fizz
5
Fizz
7
Fizz
9
Fizz
Buzz
Fizz
13
Fizz
15
Fizz
17
Fizz
19
Fizz
21
FizzBuzz
23
Fizz
25
Fizz
27
Fizz
29
Fizz
31
Fizz
Buzz
Fizz
35
Fizz
37
Fizz
39
Fizz
41
Fizz
43
FizzBuzz
45
Fizz
47
Fizz
49
Fizz
>>> 
