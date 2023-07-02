# n과 k가 주어지면 1. n에서 1을 빼거나 2. n을 k로 나눌 수 있다. n은 몇번만에 1 일 될 수 있나?

n, k = map(int,input().split())
count = 0
while n > 1:
    if n%k==0:
        n=n/k
        count = count + 1
    else:
        n = n-1
        count = count + 1

print(count)
