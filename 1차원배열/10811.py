# 바구니 뒤집기
N, M = map(int,input().split())
lst = []
for a in range(N):
    lst.append(a+1)

for i in range(M):
    a ,b = map(int,input().split())
    lst[a-1:b] = reversed(lst[a-1:b])

for i in lst:
    print(i,end=' ')
