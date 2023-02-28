# 최댓값
max_num = 0
max_idx = [0,0]

for i in range(9):
    line = list(map(int,input().split()))
    if (max(line)) > max_num :
        max_num = max(line)
        max_idx[0] = i
        max_idx[1] = line.index(max_num)

print(max_num)
print(max_idx[0]+1,max_idx[1]+1)




