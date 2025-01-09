import sys

N = int(sys.stdin.readline())
coord_lst = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    coord_lst.append((y,x))

coord_lst.sort()
for i in coord_lst:
    print(i[1],i[0])