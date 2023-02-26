# 평균은 넘겠지
import sys
c = int(input())
for i in range(c):
    inputs = list((sys.stdin.readline().split()))
    stu_num = inputs[0]
    scores = inputs[1::]
    avg = sum(scores)/int(stu_num)
    over = 0
    for score in scores:
        if int(score) > avg:
            over = over+1

    print(round(over/stu_num,3)*100)



