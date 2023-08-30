n = int(input())
works = {}

for i in range(1,n+1):
    t,p = map(int,input().split())
    works[i] = (t,p)

dp = [0] * (n+2)

for i in range(n,0,-1):
    if i + works[i][0]>n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i + 1], works[i][1] + dp[i + works[i][0]])

print(dp[1])