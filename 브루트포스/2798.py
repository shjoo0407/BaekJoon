#블랙잭

n, m = map(int,input().split())
num_list = list(map(int,input().split()))

max_sum = 0
for first in range(n):
    for second in range(first+1,n):
        for third in range(second+1,n):
            sum = num_list[first] + num_list[second] + num_list[third]
            if sum > m:
                continue
            elif sum > max_sum:
                max_sum = sum

print(max_sum)