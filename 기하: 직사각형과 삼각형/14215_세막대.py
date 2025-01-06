a,b,c = map(int,input().split())
a,b,c = sorted([a,b,c])

while True:
    if c >= a+b:
        c -= 1
    else:
        print(a+b+c)
        break

