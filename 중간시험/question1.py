def solution(size):
    
    a = [0,0,0,0,0,0]
    
    for b in size:

        if b == "XS" :
            a[0] += 1
        elif b == "S" :
            a[1] += 1
        elif b == "M" :
            a[2] += 1
        elif b == "L" :
            a[3] += 1
        elif b == "XL" :
            a[4] += 1
        elif b == "XXL" :
            a[5] += 1

    return b
                   
size_list = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(size_list)

print("solution 함수의 반환 값은 ", ret, " 입니다.")

        