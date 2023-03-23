# 분해합

n = int(input())

result = 0
for i in range(1, n+1):
    div_sum = sum(map(int, str(i)))
    if i + div_sum == n:
        result = i
        break

print(result)





