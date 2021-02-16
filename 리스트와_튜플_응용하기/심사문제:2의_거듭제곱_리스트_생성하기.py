start,end = map(int,input().split())
a = list(range(start,end+1))
listst = [2 ** i for i in a ]
del listst[1]
del listst[-2]
print(listst)
