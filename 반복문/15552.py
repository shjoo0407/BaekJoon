import sys
num = int(input())
sum = []
for i in range(num):
    a,b = sys.stdin.readline().rstrip().split()
    print(int(a)+int(b))