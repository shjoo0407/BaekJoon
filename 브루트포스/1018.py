n, m = map(int, input().split())
board = []

for i in range(n):
    row = input().strip()
    board.append(row)

min_cnt = n * m

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0


        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if board[k][l] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        min_cnt = min(min_cnt, cnt1, cnt2)

print(min_cnt)
