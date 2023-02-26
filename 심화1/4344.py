# 평균은 넘겠지
c = int(input())
for i in range(c):
    inputs = list((map(int,input().split())))
    stu_num = inputs[0]
    scores = inputs[1::]
    avg = sum(scores)/stu_num
    over = 0
    for score in scores:
        if score > avg:
            over = over+1

    print(f'{over/stu_num*100:0.3f}%')




