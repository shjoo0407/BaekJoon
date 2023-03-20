# 약수들의 합
while True:
    lst = []
    num = int(input())
    if num == -1:
        break

    for i in range(1,num):
        if num % i == 0:
            lst.append(i)
    if sum(lst) == num:
        print(num,end=' = ')
        for _ in range(len(lst)):
            if (_+1) == len(lst):
                print(lst[-1])
            else:
                print(lst[_],end=" + ")

    else:
        print(f'{num} is NOT perfect.')




