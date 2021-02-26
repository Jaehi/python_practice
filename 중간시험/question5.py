def func_a(month, day):
    
    base_month = 1
    base_day = 1
    
    day = 0
    for i in range(base_month,month+1):
        if base_month != i:
            if i in [1,3,5,7,8,10,12]:
                day += 31
            elif i in [4,6,9,11]:
                day += 30
            else:
                day += 28
        else:
            day += day - base_day

    return day
                            
                            


def solution(start_month, start_day, end_month, end_day):
	return func_a(end_month,end_day) - func_a(start_month,start_day)

start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print("solution 함수의 반환 값은", ret, "입니다.")