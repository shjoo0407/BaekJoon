#공넣기
lst = []
bin, time = map(int,input().split())

for i in range(bin):
    lst.append(0)


for i in range(time):
    a,b,c = map(int,input().split())
    for j in range(a,b+1):
        lst[j-1] = c

for i in lst:
    print(i)

