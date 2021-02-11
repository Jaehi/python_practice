>>> #딕셔너리 키의 개수 구하기
>>> lux1 = dict(health=440,mana=220,melee=550,armor=18.72)
>>> len(lux1)
4
>>> 
>>> #연습문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
>>> camille = {
...     'health': 575.6,
...     'health_regen': 1.7,
...     'mana': 338.8,
...     'mana_regen': 1.63,
...     'melee': 125,
...     'attack_damage': 60,
...     'attack_speed': 0.625,
...     'armor': 26,
...     'magic_resistance': 32.1,
...     'movement_speed': 340
... }
>>> print(camille['health']
... )
575.6
>>> print(camille['movement_speed'])
340
>>> 
>>> #심사문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
>>> a = input().split()
health health_regen mana mana_regen
>>> b = input().split()
575.6 1.7 338.8 1.63
>>> key = list(a)
>>> value = list(map(float,b))
>>> something = dict(zip(key,value))
>>> print(something)
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}