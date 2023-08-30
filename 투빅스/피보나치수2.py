n = int(input())

fibonacci = [0] * (n + 1)
fibonacci[1] = 1

for i in range(2, n + 1):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

print(fibonacci[n])