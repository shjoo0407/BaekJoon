# 부녀회장이 될테야

# def num(k,n):
#     if k==0:
#         return n
#     else:
#         sum = 0
#         for i in range(1,n+1):
#             sum = sum + num(k-1,i)
#         return sum
#
# t = int(input())
#
# for i in range(t):
#     k = int(input())
#     n = int(input())
#     print(num(k,n))

# 백준에서는 재귀를 쓸 수 없다.

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    lst = [x for x in range(1, n+1)]

    for floor in range(k):
        for num in range(1,n):
            lst[num] = lst[num] + lst[num-1]

    print(lst[-1])


