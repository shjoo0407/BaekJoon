# 더하기 사이클
first_num = input()
cnt = 0
if int(first_num)<10:
    first_num = "0"+first_num
else:
    pass

sum = str(int(first_num[0])+int(first_num[1]))
new = first_num[-1] + sum[-1]
cnt = cnt + 1

while new != first_num:
    sum = str(int(new[0])+int(new[1]))
    new = new[-1] + sum[-1]
    cnt = cnt + 1

print(cnt)



