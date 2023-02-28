# 세로 읽기
lst = []
line_length = []
for i in range(5):
    line = list(input())
    line_length.append(len(line))
    lst.append(line)

for i in range(max(line_length)):
    for j in range(len(lst)):
        try:
            print(lst[j][i],end='')
        except:
            continue



