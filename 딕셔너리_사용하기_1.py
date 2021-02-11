>>> lux = {
...     'ket' : 'value'
... }
>>> lux = {
...     'key': 'value'
... }
>>> lux = {
...     'health' : 490,
...     'health' : 800,
...     'mana' : 334,
...     'melee' : 550,
...     'armor' : 18.72
... }
>>> print(lux)
{'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> 
>>> 
>>> x = {
...     100 : 'hundred',
...     False : 0,
...     3.5 : [3.5,3.5]
...      }
>>> print(x)
{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
>>> #key에는 리스트와 딕셔너리를 사용할 수 없다
>>> x = {[10,20] : 100}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> print(x)
{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
>>> y = {(10,20) : 100}
>>> print(y)
{(10, 20): 100}
>>> u = {{1:'2'} : 200}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> print(u)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'u' is not defined
>>> #튜플은 사용 가능하다
>>> j = {}
>>> print(j)
{}
>>> k = dict()
>>> print(k)
{}
>>> #dick로 딕셔너리 만들기
>>> lux1 = dict(health=440,mana=220,melee=550,armor=18.72)
>>> print(lux1)
{'health': 440, 'mana': 220, 'melee': 550, 'armor': 18.72}
>>> #zip함수 사용하여 딕셔너리 만들기
>>> lux2 = dict(zip(['apple','banana','peach','melon'],[1,2,3,4]))
>>> print(lux2)
{'apple': 1, 'banana': 2, 'peach': 3, 'melon': 4}
>>> #튜플 형식으로 딕셔너리 만들기
>>> abc = dict([('a',1),('b',2),('c',3),('d',4)])
>>> print(abc)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> #dict안에 중괄호로 딕셔너리 만들기
>>> lux3 = dict({'health':550,'mana': 440,'melee':560,'armor':18.72})
>>> print(lux3)
{'health': 550, 'mana': 440, 'melee': 560, 'armor': 18.72}
>>> 
>>> #딕셔너리 키에 접근하고 값 할당하기
>>> lux3['health']
550
>>> lux3['health'] = 5000
>>> lux3['health']
5000
>>> lux3['mana'] = 9000
>>> print(lux3)
{'health': 5000, 'mana': 9000, 'melee': 560, 'armor': 18.72}
>>> lux3['regent']  = 300
>>> print(lux3)
{'health': 5000, 'mana': 9000, 'melee': 560, 'armor': 18.72, 'regent': 300}
>>> 
>>> #딕셔너리에 키가 있는지 확인하기
>>> 'attack_speed' in lux3
False
>>> 'regent' in lux3
True
>>> 
