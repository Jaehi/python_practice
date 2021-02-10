>>> a = input().split()
health mana speed armor damage
>>> b = input().split()
380.7 220.3 340 110 30.5
>>> key = list(a)
>>> value = list(map(float,b))
>>> ch = dict(zip(key,value))
>>> print(ch)
{'health': 380.7, 'mana': 220.3, 'speed': 340.0, 'armor': 110.0, 'damage': 30.5}
>>> 
