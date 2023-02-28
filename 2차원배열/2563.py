# 색종이
num = int(input())
paper = [[0] * 50]* 50

print(paper)

for i in range(num):
    x, y = map(int,input().split())
    print(x,y)
    for row in range(x,x+10):
        for col in range(y,y+10):
            paper[row][col] = 1

result = 0
for i in paper:
    result = result + i.count(1)
print(result)
# cnt = 0
# for i in range(100):
#     cnt = cnt + sum(paper[i])
#
# print(cnt)



