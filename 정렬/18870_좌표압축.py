import sys
input = sys.stdin.readline
N = int(input()) # 굳이?
num_list = list(map(int, input().split()))
new_list = sorted(num_list) # 작은 거 찾으면 되니깐 오름차순
for i in range(N):
    ans_list = [x for x in num_list if x < num_list[i]]
    print(len(set(ans_list)), end=' ')
