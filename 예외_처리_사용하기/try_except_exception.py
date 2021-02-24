y = [10,20,30]
print('a')
try:
    index,x = map(int,input('인덱스와 나눌 숫자를 입력하세요 : ').split())
    print(y[index]/x)

except ZeroDivisionError:
    print('숫자를 0으로 나눌수 없습니다.')

except IndexError:
    print('잘못된 인덱스 입니다.')