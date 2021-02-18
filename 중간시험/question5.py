# def solution(arr):

#     arr = reversed(arr)

#     return
	
# arr = [1,4,2,3]
# answer = solution(arr)

# print(answer)
arr = [1,4,2,3]
for i in arr:
    
        arr[i] = arr[i-1]

print(arr)