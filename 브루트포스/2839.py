#설탕배달

n = int(input())

min_cnt = 10000  # 가능한 봉지 수의 최댓값

for i in range((n // 5) + 1):  # 5kg짜리 봉지 개수에 대한 경우의 수
    for j in range((n // 3) + 1):  # 3kg짜리 봉지 개수에 대한 경우의 수
        if ((5 * i) + (3 * j)) == n:  # 봉지 개수 합이 n과 같으면
            if (i + j) < min_cnt:  # 봉지 수의 합이 더 작으면
                min_cnt = i + j  # 최솟값 갱신

if min_cnt == 10000:  # 봉지 개수를 못 구한 경우
    print("-1")
else:
    print(min_cnt)