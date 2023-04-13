# 커트라인
n, k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
print(lst[-k])
