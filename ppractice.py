from abc import *

class BaseCharacter(metaclass=ABCMeta):
    
    hp = 200
    hit = 10
    run = 30

    @abstractmethod
    def attack(self):
        self

    @abstractmethod
    def runn(self):
        self
    

class Minion(BaseCharacter):
    def __init__(self):
        self.hp = BaseCharacter().hp + 100
        self.hit = BaseCharacter().hit + 5
        self.run = BaseCharacter().run

    def attack(self):
        return '{0}만큼 데미지를 가했다'.format(self.hit)

    def runn(self):
        return '{0}속도로 달린다'.format(self.run)
    
    def defence(self):
        return '방어'
    

class Lulu(BaseCharacter):
    def __init__(self):
        self.hp = BaseCharacter().hp + 500
        self.hit = BaseCharacter().hit + 20
        self.run = BaseCharacter().run + 30

    def attack(self):
        return '{0}만큼 데미지를 가했다'.format(self.hit)

    def runn(self):
        return '{0}속도로 달린다'.format(self.run)

    def shield(self):
        return '보호막'

class Bbobbi(BaseCharacter):
    def __init__(self):
        self.hp = BaseCharacter().hp + 900
        self.hit = BaseCharacter().hit + 25
        self.run = BaseCharacter().run + 20

    def attack(self):
        return '{0}만큼 데미지를 가했다'.format(self.hit)

    def runn(self):
        return '{0}속도로 달린다'.format(self.run)

    def rush(self):
        return '돌진'

minion = Minion()
print('미니언으로 {0} 그리고 {1} 그리고 {2}'.format(minion.attack(),minion.defence(),minion.runn()))

lulu = Lulu()
print('룰루가 {0}을 사용했다 {1} 그리고 {2}'.format(lulu.shield(),lulu.attack(),lulu.runn()))

bbobbi = Bbobbi()
print('뽀삐가 {0}했다 {1} 그리고 {2}'.format(bbobbi.rush(), bbobbi.attack(), bbobbi.runn()))
i = 0
lulu_run = 1100
bbobbi_run  = 1500
run_count = 0


# while True:
    
#     bbobbi.hp  = bbobbi.hp - minion.hit
#     print(bbobbi.hp)

#     if bbobbi.hp < 0:
#         break

#     i += 1
#     print(i)

# while True:

#     lulu_run = lulu_run + lulu.run
#     bbobbi_run = bbobbi_run + bbobbi.run
    
#     if lulu_run >= 3000 or bbobbi_run >= 3000:
#         if lulu_run > bbobbi_run:
#             print('lulu')
#         else:
#             print('bbobbi')
#         break
    
#     run_count += 1

#     print()

while True:
    lulu_run = lulu_run + lulu.run
    bbobbi_run = bbobbi_run + bbobbi.run

    if lulu_run > bbobbi_run:
        print(lulu_run)
        break


    