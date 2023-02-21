#공바꾸기


bin, time = map(int,input().split())
lst = [int(i+1) for i in range(bin)]

for i in range(time):
    a,b = map(int,input().split())
    lst[a-1], lst[b-1] = lst[b-1],lst[a-1]


for i in lst:
    print(i,end=' ')
