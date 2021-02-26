N = int(input())
 
i = 0
fivehun_result = 1
onehun_result = 1
fifty_result = 1
ten_result = 1


while True:
    N = N - 500
    if N < 500:
        break

    fivehun_result += 1

print(fivehun_result)
print(N)

while True:
    N = N - 100
    if N < 100:
        break
    
    onehun_result += 1
print(onehun_result)
print(N)

while True:
    N = N - 50
    if N < 50:
        break
    fifty_result += 1

print(fifty_result)
print(N)

while True:
    N = N - 10
    if N == 0:
        break
    ten_result += 1

print(ten_result)
print(N)

print(fivehun_result+onehun_result+fifty_result+ten_result)