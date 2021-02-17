text = str(input())
y = 0
vv = text.split()
for i in vv:
    i = i.strip('.,')
    if len(i) == 3 and i =='the':
        y += 1

print(y)