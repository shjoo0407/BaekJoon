N = int(input())

i = 2
while i * i <= N:  # i가 N의 제곱근 이하일 때까지 반복
    while N % i == 0:  # N이 i로 나누어떨어지면
        print(i)  # i는 소인수
        N //= i  # N을 i로 나눔
    i += 1  # 다음 후보로 이동

if N > 1:  # 마지막으로 남은 값이 1보다 크다면 소수임
    print(N)