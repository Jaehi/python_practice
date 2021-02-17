a = [[1,2],[3,4],[5,6]]
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j],end = " ")
        j += 1
    print()
    i += 1
