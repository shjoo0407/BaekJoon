n, m = map(int,input().split())
min_nums = []
for i in range(n):
    nums = list(map(int,input().split()))
    num_min = min(nums)
    min_nums.append(num_min)

print(max(min_nums))

