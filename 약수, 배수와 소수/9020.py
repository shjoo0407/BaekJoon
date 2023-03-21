# 골드바흐의 추측
t = int(input())

for i in range(t):
    num = int(input())
    sosu_lst = []
    for a in range(3,num+1):
        for b in range(2,a+1):
            if a % b == 0:
                break
            elif b == a-1:
                sosu_lst.append(a)

    print(sosu_lst)

    ans_lst = []
    for a in range(len(sosu_lst)//2):
        for b in range(len(sosu_lst)-(a+1)):
            if (sosu_lst[a] + sosu_lst[b]) == num:
                print(sosu_lst[a],sosu_lst[b])
                ans_lst.append((sosu_lst[a],sosu_lst[b]))

    print(ans_lst)


