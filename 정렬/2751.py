# 수 정렬하기
import sys
input = sys.stdin.readline()

n = int(input)
nums = [int(input) for _ in range(n)]
nums.sort()

for i in nums:
    print(i)