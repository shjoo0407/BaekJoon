# 수 정렬하기

n = int(input())

#버블정렬
m = []
for i in range(n):
    m.append(int(input()))

for i in range(len(m)):
    for j in range(len(m)):
        if m[i]<m[j]:
            m[i],m[j] = m[i],m[j]

for i in m:
    print(i)

#삽입정렬
# m = []
# for i in range(n):
#     m.append(int(input()))
#
# for i in range(1,len(m)):
#     while(i>0)&(m[i]<m[i-1]):
#         m[i],m[i-1] = m[i-1],m[i]
#
#         i = i + 1
# for i in m:
#     print(i)