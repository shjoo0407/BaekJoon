#소수
m = int(input())
n = int(input())
sosu_lst = []
for i in range(m,n+1):
    for j in range(3,i+1):
        if i%j==0:
            break
        elif j == i-1:
            sosu_lst.append(i)

if len(sosu_lst) == 0:
    print(-1)
else:
    print(sum(sosu_lst))
    print(min(sosu_lst))

