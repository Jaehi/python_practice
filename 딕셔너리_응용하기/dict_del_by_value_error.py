#오류
x = {'a':10,'b':20,'c':30,'d':40}
# for key, value in x.items():
#     if valie == 20:
#         del x[key]
# print(x)

#if조건문 사용하여 삭제하기
x = {key:value for key,value in x.items() if value != 20}
print(x)