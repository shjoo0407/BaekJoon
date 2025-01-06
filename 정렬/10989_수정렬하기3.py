import sys

# 계수 정렬 버전
N = int(sys.stdin.readline())
count = [0] * 10001
for i in range(N):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)

# Quick sort 버전 - TODO : 여전히 메모리 부족

# def quick_sort(num_list):
#     if len(num_list) <= 1:
#         return num_list
#
#     pivot = len(num_list) // 2
#     left = [x for x in num_list if x < pivot]
#     middle = [x for x in num_list if x == pivot]
#     right = [x for x in num_list if x > pivot]
#
#     return quick_sort(left) + middle + quick_sort(right)
#
# N = int(sys.stdin.readline())
# num_list = []
# for i in range(N):
#     num = int(sys.stdin.readline())
#     num_list.append(num)
#
# num_list = quick_sort(num_list)
# for i in num_list:
#     print(i)

