# 수 정렬하기2
import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in lst:
    print(i)
