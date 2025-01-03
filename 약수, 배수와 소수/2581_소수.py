#소수
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

m = int(input())
n = int(input())

primes = [num for num in range(m,n+1) if is_prime(num)]

if primes:
    print(sum(primes))
    print(min(primes))

else:
    print('-1')