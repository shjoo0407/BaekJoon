xs, ys = [], []
for i in range(3):
    a,b = map(int,input().split())
    xs.append(a)
    ys.append(b)


for x in xs:
    if xs.count(x) == 1:
        print(x, end=' ')

for y in ys:
    if ys.count(y) == 1:
        print(y)




