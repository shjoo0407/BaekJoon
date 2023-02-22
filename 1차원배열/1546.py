# 평균

N = int(input())
scores = list(map(int,input().split()))
max_num = max(scores)
for j in range(len(scores)):
        scores[j] = scores[j]/max_num*100
print(sum(scores)/len(scores))

