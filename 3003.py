user = list(map(int,input().split()))
answer = [1,1,2,2,2,8]

for i in range(6):
    cha = answer[i]-user[i]
    print(cha,end=' ')
