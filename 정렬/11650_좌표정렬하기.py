import sys
input = sys.stdin.readline
N = int(input())
coord_list = []

for i in range(N):
    x,y = map(int, input().split())
    coord_list.append((x,y))

coord_list.sort()
for i in coord_list:
    print(i[0],i[1])
