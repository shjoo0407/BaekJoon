# 너의 평점은
scores = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
real_score = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
sum = 0
b_sum = 0
for i in range(20):
    a,b,c = input().split()
    if c == 'P':
        continue
    index = scores.index(c)
    score = real_score[index]
    sum = sum + (score*float(b))
    b_sum = b_sum + float(b)
print(f'{sum/b_sum:0.6f}')
