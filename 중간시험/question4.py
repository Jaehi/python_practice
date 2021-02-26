def solution(arr, max_n, min_n):
    number_count_dict = {}

    for i in arr:
        if str(i) in number_count_dict.keys():
            number_count_dict[str(i)] += 1
        else:
            number_count_dict[str(i)] = 1

    answer = number_count_dict[str(max_n)] // number_count_dict[str(min_n)]

    return answer

arr = [1,2,3,3,1,3,3,2,3,2]
max_num = max(arr)
min_num = min(arr)  
answer = solution(arr, max_num, min_num)

print(max_num,"이", min_num,"보다 ", answer,"배 많이 들어있다.")
