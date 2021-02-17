a = [3,1,3,2,5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

#이런 방법도 있지
c = [[0]*i for i in [3,1,3,2,5]]
print(c)
