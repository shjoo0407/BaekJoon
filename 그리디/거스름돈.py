# 거스름돈
# 남은 돈이 n원일 때 동전의 개수 세기
n = int(input())
count = 0
coins = [500,100,50,10]

for coin in coins :
    count = count + (n // coin)
    n = n % coin

print(count)


