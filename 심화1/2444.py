# 별찍기 -7
N = int(input())

for a in range(1,N+1):
    print(' '*(N-a)+'*'*(2*a-1))
for a in range(N-1,0,-1):
    print(' '*(N-a)+"*"*(2*a-1))



