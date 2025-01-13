# 탐색 - 큰 배열이 있을 때 효율적으로 비교 탐색이 가능한가?
import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split()))

num_dict = {}
for i in range(N):
    num_dict[n_list[i]] = 0

for j in range(M):
    if m_list[j] in num_dict:
        print('1', end=' ')
    else:
        print('0', end=' ')