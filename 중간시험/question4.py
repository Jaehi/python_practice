def solution(arr, max_n, min_n):
    max_n = max_n//min_n
    return max_n

	

arr = [1,2,3,3,1,3,3,2,3,2]
max_num = max(arr)
min_num = min(arr)  
answer = solution(arr, max_num, min_num)

print(max_num,"이", min_num,"보다 ", answer,"배 많이 들어있다.")
