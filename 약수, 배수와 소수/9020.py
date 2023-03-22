# 골드바흐의 추측

# 소수 판별하는 코드 함수로 따로 빼기
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    half_n = n//2
    a = half_n
    b = half_n
    for i in range(half_n, 1, -1):
        if is_prime(i) and is_prime(n - i):
            a = i
            b = n - i
            break
    print(a, b)


