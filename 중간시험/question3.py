def func_a(month, day):
    a = 0
    list = [31,28,31,30,31,30,31,31,30,31,30,31]
	
    for i in range(month - 1):
        a += list[i]
    a += day
    return a - 1

def solution(start_month, start_day, end_month, end_day):

    b = func_a(start_month,start_day)

    c = func_a(end_month,end_day)

    return c - b
	

start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print("solution 함수의 반환 값은", ret, "입니다.")