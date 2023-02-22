# 과제 안내신분..?
lst = []
for a in range(30):
    lst.append(a+1)

for i in range(28):
    a = int(input())
    lst.remove(a)

for a in lst:
    print(a)