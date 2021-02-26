# def solution(arr, max_n, min_n):
    
# 	pass

# arr = [1,2,3,3,1,3,3,2,3,2]
# max_num = max(arr)
# min_num = min(arr)  
# answer = solution(arr, max_num, min_num)

# print(max_num,"이", min_num,"보다 ", answer,"배 많이 들어있다.")

def solution(shirt_size):
	
	llist = [0,0,0,0,0,0]

	for i in shirt_size:
    			
		if i == 'XS':
    			llist[0] += 1
		elif i == 'S':
    			llist[1] += 1
		elif i == 'M':
				llist[2] += 1
		elif i == 'L':
    			llist[3] += 1
		elif i == 'XL':
    			llist[4] += 1
		elif i == 'XXL':
    			llist[5] += 1
	return i

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);    # shirt_size를 매개변수로 넘겨주면서 solution함수를 호출하고 리턴값을 ret에 저장합니다.

print("solution 함수의 반환 값은 ", ret, " 입니다.")