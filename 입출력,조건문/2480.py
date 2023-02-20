#주사위 세개
a,b,c = map(int,input().split())
price = 0
if (a==b) & (a==c):
    price = 10000+(a*1000)
elif (a==b) | (a==c):
    price = 1000 + (a*100)
elif (b==c):
    price = 1000 + (b*100)
else:
    price = max(a,b,c) * 100

print(price)

