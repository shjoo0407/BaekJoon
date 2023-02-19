a,b = map(int,input().split())
c = int(input())

mok = (b+c)//60
a = a+mok

c = (b+c)%60

if a >= 24:
    a = a-24

print(a,c)


