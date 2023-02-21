lst = []
for a in range(9):
    num = int(input())
    lst.append(num)

max = 0
idx = 0
for i in range(len(lst)):
    if lst[i]>max:
        max = lst[i]
        idx = i
    else:
        pass
print(max)
print(idx+1)