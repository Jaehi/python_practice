q, w = map(int, input().split())
a = { i+1 for i in range(q) if q%(i+1)==0} 
b = { i+1 for i in range(w) if w%(i+1)==0}

divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)