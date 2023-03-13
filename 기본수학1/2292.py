# 벌집
num = int(input())

floor = 1
i = 1

while i<num:
    i = i + (floor * 6)
    floor = floor + 1

print(floor)